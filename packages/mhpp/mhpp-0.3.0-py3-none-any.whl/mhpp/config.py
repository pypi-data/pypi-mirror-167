import os

""" Default folder paths Configuration """


class DefaultConfig:
    """
        Default folder paths Configuration.
        Assuming having create dir access.
    """
    
    DATA_RAW_PATH = os.path.expanduser("~/defaults/data/raw")
    os.makedirs(DATA_RAW_PATH, exist_ok=True)
    DATA_PROCESSED_PATH = os.path.expanduser("~/defaults/data/processed")
    os.makedirs(DATA_PROCESSED_PATH, exist_ok=True)
    MODELS_PATH = os.path.expanduser("~/defaults/data/model_pkls")
    os.makedirs(MODELS_PATH, exist_ok=True)
    TRAIN_TEST_DATA = os.path.expanduser("~/defaults/data/train_test_data")
    os.makedirs(TRAIN_TEST_DATA, exist_ok=True)