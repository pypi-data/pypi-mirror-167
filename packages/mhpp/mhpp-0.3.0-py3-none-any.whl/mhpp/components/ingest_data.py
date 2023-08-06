# -*- coding: utf-8 -*-
"""This module is to help fetch, preprocess and split the data into train and test datasets.
It can be used from both terminal and as well as code.
"""


import os
import sys
import argparse
import tarfile
import numpy as np
import pandas as pd
import pathlib
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from six.moves import urllib
from mhpp.loggers import loggerWrapper
from mhpp.config import DefaultConfig
from mhpp.utils import timestamp
from mhpp.cli.cmd_args import (
    add_data_path_arg,
    add_processed_path_arg,
    add_train_test_data_path_arg,
    add_logger_args
)

CONFIG = DefaultConfig()

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
DEFAULT_HOUSING_PATH = CONFIG.DATA_RAW_PATH
DEFAULT_DATA_PROCESSED_PATH = CONFIG.DATA_PROCESSED_PATH
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=DEFAULT_HOUSING_PATH, 
                   logger = None
):
    """Accessing through terminal:

    usage: fetch-data [-h] [-dp DATA_PATH] [-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-lp LOG_PATH] [-ncl]

    For fetching housing data from the https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz and
    downloading it to local.

    optional arguments:

    **-h, --help** : show this help message and exit.
    
    **-dp DATA_PATH, --data-path DATA_PATH** : To take input path from user to download the fetched data.
    
    **-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}** : To take input from user for specific log level.
    
    **-lp LOG_PATH, --log-path LOG_PATH** : To take input from user for log path to save logs.
    
    **-ncl, --no-console-log**  To take input from user for setting console log.

    Below explains the *Parameters*

    Parameters
    ----------
    housing_path : pathlib.Path
        [Optional] Path to save the data.

    Below is the *Return* type

    Returns
    -------
    None
        returns None
    """
    try:
        
        if not logger:
            parser = argparse.ArgumentParser(
                description=f"For fetching housing data from the {HOUSING_URL} \n and downloading it to local."
            )
            add_data_path_arg(parser)
            add_logger_args(parser)
            args = parser.parse_args()
            if args.data_path != DEFAULT_HOUSING_PATH:
                housing_path = args.data_path
    
            logger = loggerWrapper(
                        args.log_level, args.log_path, args.no_console_log
                )
        
        tgz_path = os.path.join(housing_path, "housing.tgz")
        urllib.request.urlretrieve(housing_url, tgz_path)
        logger.debug(f"Downloaded dataset to location {tgz_path}....Success")
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        logger.debug(f"Extarcted dataset to location {housing_path}....Success")
        housing_tgz.close()
        logger.debug(f"Fetching Success!!!! Please check the {housing_path} for the files.")
    except Exception as e:
        logger.error(f"Failed!!! Error......... {e}")


def load_housing_data(logger, housing_path=DEFAULT_HOUSING_PATH):
    try:
        fetch_housing_data(housing_path=housing_path, logger=logger)
        csv_path = os.path.join(housing_path, "housing.csv")
        logger.debug("Loading Success!!!!\ncsv loaded")
        return pd.read_csv(csv_path)
    except Exception as e:
        logger.error(f"Failed!!! Error......... {e}")
        return None


def preprocessing(
    logger, housing_path=DEFAULT_HOUSING_PATH, 
    processed_path=DEFAULT_DATA_PROCESSED_PATH 
):
    try:

        housing = load_housing_data(housing_path=housing_path, logger=logger)
        logger.debug("Preprocessing Started.")
        labels = housing["median_house_value"]
        housing = housing.drop("median_house_value", axis=1)
        housing["income_cat"] = pd.cut(
            housing["median_income"],
            bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
            labels=[1, 2, 3, 4, 5],
        )

        imputer = SimpleImputer(strategy="median")
        housing_cat = housing["ocean_proximity"]
        housing_num = housing.drop("ocean_proximity", axis=1)
        imputer.fit(housing_num)
        X = imputer.transform(housing_num)
        housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
        housing_prepared = housing_tr.join(pd.get_dummies(housing_cat, drop_first=True))
        logger.debug("Preprocessing Completed.")
        
        logger.debug(f"Saving features and labels to {processed_path} folder...Starts")
        tstamp = timestamp()
        housing_prepared.to_csv(f"{processed_path}/{tstamp}_features.csv", index=False)
        logger.debug(f"Saved features to path {processed_path}/{tstamp}_features.csv")
        labels.to_csv(f"{processed_path}/{tstamp}_labels.csv", index=False)
        logger.debug(f"Saved labels to path {processed_path}/{tstamp}_labels.csv")
        
        return {
            "success": True,
            "data": {
                "features": housing_prepared,
                "labels": labels,
                "timestamp": tstamp,
                "fetures_path": f"{processed_path}/{tstamp}_features.csv",
                "labels_path": f"{processed_path}/{tstamp}_labels.csv",
            },
        }
    except Exception as e:
        logger.error(f"Failed.... Error......... {e}")
        return {"success": False, "error": str(e)}


def train_test_data(
    housing_path=DEFAULT_HOUSING_PATH,
    processed_path=DEFAULT_DATA_PROCESSED_PATH,
    train_test_data_path = CONFIG.TRAIN_TEST_DATA,
    **kwargs,
):
    """Accessing through terminal:

    usage: train-test-data [-h] [-dp DATA_PATH] [-pp PROCESSED_PATH] [-ttp TRAIN_TEST_DATA_PATH]
                    [-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-lp LOG_PATH] [-ncl]

    Take both data output and processed path from the user.

    optional arguments:

    **-h, --help** : show this help message and exit

    **-dp DATA_PATH, --data-path DATA_PATH** :  To take input path from user to download the fetched data.

    **-pp PROCESSED_PATH, --processed-path PROCESSED_PATH** : To take input path from user to save the processed data

    **-ttp TRAIN_TEST_DATA_PATH, --train-test-data-path TRAIN_TEST_DATA_PATH** : To take output data path for saving the train and test data.

    **-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}** : To take input from user for specific log level.

    **-lp LOG_PATH, --log-path LOG_PATH** :  To take input from user for log path to save logs.
    
    **-ncl, --no-console-log** :  To take input from user for setting console log.

    Below are the *parameters*

    Parameters
    ----------
        housing_path : pathlib.Path
            [Optional] Path to read the data.
        processed_path : pathlib.Path
            [Optional] Path to save the processed data.
        train_test_data_path : pathlib.Path
            [Optional] Path to save the train and test datasets.
        kwargs : dict
            *kwargs* contains the following keys
                *features* : to take input features as np.array.

                *labels*  : to take input labels as np.array.

                timestamp: timestamp of the features and labels when preprocessed.

    Below is the *return* type

    Returns
    -------        
    dict
        returns a dict.
        Below is the payload with its explanations

            {
                "success": True, # implies if the train and test data preparation success or not.
                "data": {
                    "X_train": X_train, # numpy array containing train features

                    "X_test": X_test,   # numpy array containing test features

                    "y_train": y_train, # numpy array containing train labels

                    "y_test": y_test,   # numpy array containing test labels

                    "saved_path": path, # path where the train test datasets are stored.
                },
            }
         -------
        ``Note:`` The preprocessed files are given name in this format.

            **{timestamp}_features.csv** for features
            **{timestamp}_labels.csv** for labels

            Therefore the folder containing the train and test datasets is the timestamp.
            This is how the above timestamp parameter is used for.
    """
    
    try:
        X = []
        y = []
        tstamp = ""
        show = True
        if not (kwargs.get("features", None) and kwargs.get("labels", None)):
            parser = argparse.ArgumentParser(
                description="Preprocessing and splitting the data into train and test datasets and saving them to a directory."
            )
            add_data_path_arg(parser)
            add_processed_path_arg(parser)
            add_train_test_data_path_arg(parser)
            add_logger_args(parser)
            args = parser.parse_args()

            logger = loggerWrapper(
                        args.log_level, args.log_path, args.no_console_log
                )

            if args.processed_path != DEFAULT_DATA_PROCESSED_PATH:
                processed_path = args.processed_path
            if args.data_path != DEFAULT_HOUSING_PATH:
                housing_path = args.data_path
                
            if args.train_test_data_path != CONFIG.TRAIN_TEST_DATA:
                train_test_data_path = args.train_test_data_path
            data = preprocessing(logger, housing_path, processed_path)
            if data.get("success"):
                data = data.get("data")
                X = data.get("features")
                y = data.get("labels")
                tstamp = data.get("timestamp")
                show = False
            else:
                sys.exit(0)
        else:
            logger = loggerWrapper(
                        kwargs.get("log_level", "DEBUG"), 
                        kwargs.get("log_path", None), 
                        kwargs.get("no_console_log", False)
                )
            X = kwargs.get("features")
            y = kwargs.get("labels")
            tstamp = kwargs.get("timestamp")
        
        logger.debug("Splitting the data to train test split....Started.")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=kwargs.get("test_size", 0.2), random_state=42
        )
        logger.debug("Splitting the data to train test split....Done.")
        # saving the train and val data
        path = os.path.join(train_test_data_path, tstamp)
        logger.debug(f"Saving the train and test data to {path}....Started.")
        os.makedirs(path, exist_ok=True)
        X_train.to_csv(os.path.join(path, "X_train.csv"), index=False)
        X_test.to_csv(os.path.join(path, "X_test.csv"), index=False)
        y_train.to_csv(os.path.join(path, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(path, "y_test.csv"), index=False)
        logger.debug(f"Saving the train and test data to {path}....Done.")
        
        if show:
            return {
                "success": True,
                "data": {
                    "X_train": X_train,
                    "X_test": X_test,
                    "y_train": y_train,
                    "y_test": y_test,
                    "saved_path": path,
                },
            }
    except Exception as e:
        logger.error(f"Failed.... Error......... {e}")
        if show:
            return {"success": False, "error": str(e)}
