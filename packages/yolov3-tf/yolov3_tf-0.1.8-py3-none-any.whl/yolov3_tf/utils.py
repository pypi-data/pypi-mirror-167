import logging
from typing import List, Union

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.parsing_config import (
    FixedLenFeature,
    FixedLenSequenceFeature,
    VarLenFeature,
)

YOLOV3_LAYER_LIST = [
    "yolo_darknet",
    "yolo_conv_0",
    "yolo_output_0",
    "yolo_conv_1",
    "yolo_output_1",
    "yolo_conv_2",
    "yolo_output_2",
]

YOLOV3_TINY_LAYER_LIST = [
    "yolo_darknet",
    "yolo_conv_0",
    "yolo_output_0",
    "yolo_conv_1",
    "yolo_output_1",
]


def load_darknet_weights(model, weights_file, tiny=False):
    wf = open(weights_file, "rb")
    major, minor, revision, seen, _ = np.fromfile(wf, dtype=np.int32, count=5)

    if tiny:
        layers = YOLOV3_TINY_LAYER_LIST
    else:
        layers = YOLOV3_LAYER_LIST

    for layer_name in layers:
        sub_model = model.get_layer(layer_name)
        for i, layer in enumerate(sub_model.layers):
            if not layer.name.startswith("conv2d"):
                continue
            batch_norm = None
            if i + 1 < len(sub_model.layers) and sub_model.layers[
                i + 1
            ].name.startswith("batch_norm"):
                batch_norm = sub_model.layers[i + 1]

            logging.info(
                "{}/{} {}".format(
                    sub_model.name, layer.name, "bn" if batch_norm else "bias"
                )
            )

            filters = layer.filters
            size = layer.kernel_size[0]
            in_dim = layer.get_input_shape_at(0)[-1]

            if batch_norm is None:
                conv_bias = np.fromfile(wf, dtype=np.float32, count=filters)
            else:
                # darknet [beta, gamma, mean, variance]
                bn_weights = np.fromfile(
                    wf, dtype=np.float32, count=4 * filters
                )
                # tf [gamma, beta, mean, variance]
                bn_weights = bn_weights.reshape((4, filters))[[1, 0, 2, 3]]

            # darknet shape (out_dim, in_dim, height, width)
            conv_shape = (filters, in_dim, size, size)
            conv_weights = np.fromfile(
                wf, dtype=np.float32, count=np.product(conv_shape)
            )
            # tf shape (height, width, in_dim, out_dim)
            conv_weights = conv_weights.reshape(conv_shape).transpose(
                [2, 3, 1, 0]
            )

            if batch_norm is None:
                layer.set_weights([conv_weights, conv_bias])
            else:
                layer.set_weights([conv_weights])
                batch_norm.set_weights(bn_weights)

    assert len(wf.read()) == 0, "failed to read all data"
    wf.close()


def broadcast_iou(box_1, box_2):
    # box_1: (..., (x1, y1, x2, y2))
    # box_2: (N, (x1, y1, x2, y2))

    # broadcast boxes
    box_1 = tf.expand_dims(box_1, -2)
    box_2 = tf.expand_dims(box_2, 0)
    # new_shape: (..., N, (x1, y1, x2, y2))
    new_shape = tf.broadcast_dynamic_shape(tf.shape(box_1), tf.shape(box_2))
    box_1 = tf.broadcast_to(box_1, new_shape)
    box_2 = tf.broadcast_to(box_2, new_shape)

    int_w = tf.maximum(
        tf.minimum(box_1[..., 2], box_2[..., 2])
        - tf.maximum(box_1[..., 0], box_2[..., 0]),
        0,
    )
    int_h = tf.maximum(
        tf.minimum(box_1[..., 3], box_2[..., 3])
        - tf.maximum(box_1[..., 1], box_2[..., 1]),
        0,
    )
    int_area = int_w * int_h
    box_1_area = (box_1[..., 2] - box_1[..., 0]) * (
        box_1[..., 3] - box_1[..., 1]
    )
    box_2_area = (box_2[..., 2] - box_2[..., 0]) * (
        box_2[..., 3] - box_2[..., 1]
    )
    return int_area / (box_1_area + box_2_area - int_area)


def draw_outputs(img, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    boxes, objectness, classes, nums = (
        boxes[0],
        objectness[0],
        classes[0],
        nums[0],
    )
    wh = np.flip(img.shape[0:2])
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(
            img,
            "{} {:.4f}".format(class_names[int(classes[i])], objectness[i]),
            x1y1,
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0, 0, 255),
            2,
        )
    return img


def draw_labels(x, y, class_names):
    img = x.numpy()
    boxes, classes = tf.split(y, (4, 1), axis=-1)
    classes = classes[..., 0]
    wh = np.flip(img.shape[0:2])
    for i in range(len(boxes)):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(
            img,
            class_names[classes[i]],
            x1y1,
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (0, 0, 255),
            2,
        )
    return img


def freeze_all(model, frozen=True):
    model.trainable = not frozen
    if isinstance(model, tf.keras.Model):
        for layer in model.layers:
            freeze_all(layer, frozen)


def int_feature(
    allow_missing: bool = True,
    fixed_len: bool = True,
    dtype: tf.dtypes.DType = tf.int64,
) -> Union[FixedLenSequenceFeature, VarLenFeature]:
    if fixed_len:
        return tf.io.FixedLenSequenceFeature(
            [], dtype=tf.int64, allow_missing=allow_missing
        )
    return tf.io.VarLenFeature(dtype=dtype)


def float_feature(
    allow_missing: bool = True,
    fixed_len: bool = True,
    dtype: tf.dtypes.DType = tf.float32,
) -> Union[FixedLenSequenceFeature, VarLenFeature]:
    if fixed_len:
        return tf.io.FixedLenSequenceFeature(
            [], dtype=tf.float32, allow_missing=allow_missing
        )
    return tf.io.VarLenFeature(dtype=dtype)


def string_feature(
    fixed_len: bool = True,
) -> Union[FixedLenFeature, VarLenFeature]:
    if fixed_len:
        return tf.io.FixedLenFeature([], dtype=tf.string)
    return tf.io.VarLenFeature(dtype=tf.string)


def flatten_list(x: list) -> list:
    return [item for sublist in x for item in sublist]


def to_dense(x: tf.Tensor) -> np.ndarray:
    return tf.sparse.to_dense(x).numpy()


def read_content(path: str) -> bytes:
    """
    Reads content as bytes.

    Args:
        path: content file path.

    Returns:
        Content in file as bytes.
    """
    with open(path, "rb") as stream:
        contents = stream.read()
    return contents


def encode_example(
    id_: int,
    img_path: str,
    width: List[int],
    height: List[int],
    xmin: List[float],
    ymin: List[float],
    xmax: List[float],
    ymax: List[float],
    labels: List[int],
) -> tf.train.Example:
    """
    Encode a single image path with all associated annotations as an Example.

    Args:
        id_: Unique identifier for each image.
        path: Path to the image.
        width: List of widths of bounding boxes.
        height: List of heights of bounding boxes.
        xmin: List of co-ordinate(x) top-left of the bounding boxes.
        ymin: List of co-ordinate(y) top-left of the bounding boxes.
        xmax: List of co-ordinate(x) bottom-right of the bounding boxes.
        ymax: List of co-ordinate(y) bottom-right of the bounding boxes.
        labels: List of labels of bounding boxes.

    Returns:
        Example containing all input data.
    """
    return tf.train.Example(
        features=tf.train.Features(
            feature={
                "image/id": tf.train.Feature(
                    int64_list=tf.train.Int64List(value=id_)
                ),
                "image/filename": tf.train.Feature(
                    bytes_list=tf.train.BytesList(
                        value=[str(img_path.split("/")[-1]).encode("utf-8")]
                    )
                ),
                "image/encoded": tf.train.Feature(
                    bytes_list=tf.train.BytesList(
                        value=[read_content(img_path)]
                    )
                ),
                "image/width": tf.train.Feature(
                    int64_list=tf.train.Int64List(value=width)
                ),
                "image/height": tf.train.Feature(
                    int64_list=tf.train.Int64List(value=height)
                ),
                "image/bbox/xmin": tf.train.Feature(
                    float_list=tf.train.FloatList(value=xmin)
                ),
                "image/bbox/ymin": tf.train.Feature(
                    float_list=tf.train.FloatList(value=ymin)
                ),
                "image/bbox/xmax": tf.train.Feature(
                    float_list=tf.train.FloatList(value=xmax)
                ),
                "image/bbox/ymax": tf.train.Feature(
                    float_list=tf.train.FloatList(value=ymax)
                ),
                "image/bbox/labels": tf.train.Feature(
                    int64_list=tf.train.Int64List(value=labels)
                ),
            }
        )
    )
