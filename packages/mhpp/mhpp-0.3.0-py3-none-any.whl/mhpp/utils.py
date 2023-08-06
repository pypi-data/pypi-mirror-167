import os
import pathlib
import datetime
import pandas as pd
import pickle

"""
    All utils like timestamp, datetime functions.
"""


def timestamp():
    """
    returns timestamp
    """
    now = datetime.datetime.now()
    return "".join(
        [
            str(i)
            for i in [now.year, now.month, now.year, now.hour, now.minute, now.second]
        ]
    )


def verify_timestamp(timestamp, path):
    """
    check a file exists with a given timestamp.
    """
    count = sum(
        1
        for file in os.listdir(path)
        if file in [f"{timestamp}_features.csv", f"{timestamp}_labels.csv"]
    )
    if count == 2:
        return True
    if count == 1:
        return False
    return False


def get_files_with_timestamp(timestamp, path):
    """
    get the file names of both features and labels.
    """
    if verify_timestamp(timestamp):
        return {
            "success": True,
            "feature_path": os.path.join(path, f"{timestamp}_features.csv"),
            "label_path": os.path.join(path, f"{timestamp}_features.csv"),
        }
    return {
        "success": False,
    }


def load_model_frm_pkl(pkl_file_path):
    pickled_model = pickle.load(open(pkl_file_path, "rb"))
    return pickled_model


def dump_model_to_pkl(model, model_path, model_name):
    try:
        if not pathlib.Path(model_name).suffix:
            model_name = ".".join([model_name, "pkl"])
        print(model_name)
        pkl_file_path = os.path.join(model_path, model_name)
        pickle.dump(model, open(pkl_file_path, "wb"))
        return {
                "success": True,
                "model_pkl_file_path": pkl_file_path
            }
    except Exception as e:
        print(f"Failed saving model to pickel..........{e}")
    return {
            "success": False
        }


def load_csv(path):
    return pd.read_csv(path)
