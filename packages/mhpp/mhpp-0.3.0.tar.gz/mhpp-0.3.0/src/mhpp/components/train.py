# -*- coding: utf-8 -*-
"""This module is to train the model.
It can be accessed from both terminal and as code.
How to access from both terminal and as well as code 
are discussed below.
"""



import os
import sys
import argparse
from mhpp.config import DefaultConfig
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from mhpp.loggers import loggerWrapper
from mhpp.utils import timestamp, load_csv, dump_model_to_pkl
from mhpp.cli.cmd_args import (
    add_data_path_arg,
    add_pkl_path_arg,
    add_x_path_arg,
    add_y_path_arg,
    add_algo_name_arg,
    add_model_name_arg,
    add_logger_args
)


CONFIG = DefaultConfig()


def get_model(model_name, X, y):
    model = None
    if model_name == "lr":
        model = LinearRegression()
        model.fit(X, y)
    elif model_name == "dtr":
        model = DecisionTreeRegressor(random_state=42)
        model.fit(X, y)
    elif model_name == "rfr":
        model = RandomForestRegressor(random_state=42)
        model.fit(X, y)
    else:
        print("Invalid Model Name")

    return model


def train(model_path=CONFIG.MODELS_PATH, **kwargs):
    """Accessing through terminal, below are the commands:

    usage: train [-h] [-pkl PICKEL_PATH] [-x X_PATH] [-y Y_PATH] [-an {lr,dtr,rfr}] [-mn MODEL_NAME]
        [-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-lp LOG_PATH] [-ncl]

    Take train the model and save the model to a pickel file.

    optional arguments:

    **-h, --help** : show this help message and exit

    **-pkl PICKEL_PATH, --pickel-path PICKEL_PATH** : To take input directory from user to save the model pickel file.

    **-x X_PATH, --X-path X_PATH** : To take input from the user for X or features.

    **-y Y_PATH, --y-path Y_PATH** : To take input from the user for y or labels.

    **-an {lr,dtr,rfr}, --algo-name {lr,dtr,rfr}** : To take input from the user for algo name.

    **-mn MODEL_NAME, --model-name MODEL_NAME** : To take input from the user for model name.

    **-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}** : To take input from user for specific log level.

    **-lp LOG_PATH, --log-path LOG_PATH** :  To take input from user for log path to save logs.

    **-ncl, --no-console-log** : To take input from user for setting console log.

    Below are the *parameters*

    Parameters
    ----------
        model_path : pathlib.Path
            [Optional] Path where the models should be saved.
        kwargs : dict
            *kwargs* contains the following keys
                X_path: path for the features
                y_path: path for the labels
                X     : to take input features as array.
                y     : to take input labels as array.
                algo_name: Accepts values "lr", "dtr" or "rfr" (Linear Regression,
                            Decision Tree Regressor
                            and random forest regressor respectively.) algo_name determines
                            which model to be trained.
                model_name: name for the pickel file.
    
    Below is the *return* type

    Returns
    -------
        pkl
            Pickel file where the model is saved is returned.
    

    ``Note:`` Flexibilty of giving input to model in code is given as compared to 
    terminal. In code user can pass directly the numpy array for both features and labels.
    If both paths and arrays are given array overrides the path.
    """
    try:
        parser = argparse.ArgumentParser(
            description="Take train the model and save it to a pickel file."
        )
        add_pkl_path_arg(parser)
        add_x_path_arg(parser)
        add_y_path_arg(parser)
        add_algo_name_arg(parser)
        add_model_name_arg(parser)
        add_logger_args(parser)
        args = parser.parse_args()
        # print(args)
        # path to store pickel files
        if args.pickel_path != CONFIG.MODELS_PATH:
            model_path = args.pickel_path

        # algo name logic
        algo_name = "lr"
        if args.algo_name:
            algo_name = args.algo_name
        else:
            algo_name = kwargs.get("algo_name", None)

        # model name logic
        model_name = None
        if args.model_name:
            model_name = args.model_name
        else:
            model_name = kwargs.get("model_name", None)

        if not model_name or model_name=="latest":
            model_name = f"{timestamp()}_{algo_name}"

        # get X and y values.

        X, y = [], []
        show = True
        logger = loggerWrapper()
        if args.X_path and args.y_path:
            logger = loggerWrapper(
                        args.log_level, args.log_path, args.no_console_log
                )
            X, y = load_csv(args.X_path), load_csv(args.y_path)
            show = False
            logger.debug(f"Loading X and y from path {args.X_path} and {args.y_path} respectively...Done")
        elif kwargs.get("X", None) and kwargs.get("y", None):
            X, y = kwargs.get("X"), kwargs.get("y")
            logger.debug(f"Assigning X and y ...Done")
        elif kwargs.get("X_path") and kwargs.get("y_path"):
            X_path, y_path = kwargs.get("X_path"), kwargs.get("y_path")
            X, y = load_csv(X_path), load_csv(y_path)
            logger.debug(f"Loading X and y from path {X_path} and {y_path} respectively...Done")
        else:
            print("Missing file path for X or y")
            sys.exit(0)

        logger.debug(f"Training started.")
        model = get_model(algo_name, X, y)
        if model:
            result = dump_model_to_pkl(model, model_path, model_name)
            if result.get("success"):
                logger.debug("Training Successfully completed.!!!!")
                logger.debug(
                    f"Check for {model_name} model in path {result.get('model_pkl_file_path')}"
                )
                if show:
                    return {"model_pkl_file_path": result.get("model_pkl_file_path")}
        return None
    except Exception as e:
        logger.error(f"Training failed....{e}")
        return None
