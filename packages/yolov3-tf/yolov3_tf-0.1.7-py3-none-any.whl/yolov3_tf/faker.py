import os
import tempfile
import uuid
from random import randint

import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from utils import encode_example


def fake_image(image_size):
    random_array = np.random.random_sample(image_size) * 255
    random_array = random_array.astype(np.uint8)
    return random_array


def fake_labels(n_classes, max_boxes, image_size):
    labels = []
    for _ in range(randint(1, max_boxes)):
        image_bbox = [0, 0, image_size[0], image_size[1]]
        v = [randint(0, max(image_bbox)) for v in image_bbox]
        left = min(v[0], v[2])
        upper = min(v[1], v[3])
        right = max(v[0], v[2])
        lower = max(v[1], v[3])
        bbox = [left, upper, right, lower]
        k = randint(1, n_classes)
        label = [k] + bbox
        labels.append(label)
    return labels


def fake_annotations_dataframe(
    n, image_size=(416, 416, 3), n_classes=3, max_boxes=5
):
    image_dir = tempfile.mkdtemp()
    records = []
    columns = [
        "id",
        "file_name",
        "width",
        "height",
        "x_min",
        "y_min",
        "x_max",
        "y_max",
        "label",
    ]
    for _ in range(n):
        image_array = fake_image(image_size)
        raw_image = Image.fromarray(image_array)
        image_filename = str(uuid.uuid4()) + ".png"
        image_path = os.path.join(image_dir, image_filename)
        raw_image.save(image_path)
        labels = fake_labels(n_classes, max_boxes, image_size)
        for label in labels:
            class_id, xmin, ymin, xmax, ymax = label
            records.append(
                (
                    image_path,
                    image_size[0],
                    image_size[1],
                    xmin,
                    ymin,
                    xmax,
                    ymax,
                    class_id,
                )
            )
    dataframe = pd.DataFrame(records)
    dataframe = dataframe.reset_index()
    dataframe.columns = columns
    return dataframe


def fake_tfrecords(n, image_size=(416, 416, 3), n_classes=3, max_boxes=5):
    dataframe = fake_annotations_dataframe(n, image_size, n_classes, max_boxes)
    file_names = list(dataframe["file_name"].unique())
    target = os.path.join(tempfile.mkdtemp(), "sample.tfrecords")
    with tf.io.TFRecordWriter(str(target)) as writer:
        for idx, file_name in enumerate(file_names):
            df_image = dataframe.loc[dataframe["file_name"] == file_name]
            id_ = [idx]
            width = df_image["width"].to_numpy().astype(int)
            height = df_image["height"].to_numpy().astype(int)
            xmin = df_image["x_min"].to_numpy()
            ymin = df_image["y_min"].to_numpy()
            xmax = df_image["x_max"].to_numpy()
            ymax = df_image["y_max"].to_numpy()
            labels = df_image["label"].to_numpy().astype(int)
            example = encode_example(
                id_, file_name, width, height, xmin, ymin, xmax, ymax, labels
            )
            writer.write(example.SerializeToString())
    return target
