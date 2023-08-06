"""This module is to evaluate the model.
It can be accessed from both terminal and as code.
It takes the pickel file path, features and label paths or arrays(only in case 
through code), metric and returns the score or the metric value.
"""



import sys
import argparse
import numpy as np
from mhpp.config import DefaultConfig
from mhpp.loggers import loggerWrapper
from sklearn.metrics import mean_squared_error, mean_absolute_error
from mhpp.utils import load_model_frm_pkl, load_csv
from mhpp.cli.cmd_args import (
    add_model_pkl_file_path_arg,
    add_x_path_arg,
    add_y_path_arg,
    add_mertic_arg,
    add_logger_args,
)


CONFIG = DefaultConfig()


def get_score(metric, y, y_pred):
    score = None
    if metric == "mse":
        score = mean_squared_error(y, y_pred)
    elif metric == "mas":
        score = mean_absolute_error(y, y_pred)
    elif metric == "rmse":
        score = np.sqrt(mean_squared_error(y, y_pred))
    else:
        print("Invalid Metric")
    return score


def evaluate(model_pkl_file_path=None, **kwargs):
    """Accessing through terminal, below are the commands:

    usage: evaluate [-h] [-m {mse,rmse,mas,all}] [-mpkl MODEL_PKL_FILE_PATH] [-x X_PATH] [-y Y_PATH]
    [-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-lp LOG_PATH] [-ncl]

    Take the model path, processed path and timestamp from the user.

    optional arguments:
    **-h, --help** : show this help message and exit

    **-m {mse,rmse,mas,all}, --metric {mse,rmse,mas,all}** : To take input metric from the user to evaluate the model.

    **-mpkl MODEL_PKL_FILE_PATH, --model-pkl-file-path MODEL_PKL_FILE_PATH** : To take input from the user for reading the model pickel file path.

    **-x X_PATH, --X-path X_PATH** : To take input from the user for X or features.
    
    **-y Y_PATH, --y-path Y_PATH** :  To take input from the user for y or labels.

    **-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}** : To take input from user for specific log level.

    **-lp LOG_PATH, --log-path LOG_PATH** : To take input from user for log path to save logs.

    **-ncl, --no-console-log** : To take input from user for setting console log.

    Below are the *parameters*.
    
    Parameters
    ----------
        model_pkl_file_path : pathlib.Path
            [Optional] Path of the pickel file.
        kwargs : dict
            kwargs contains the following keys:
                X_path: path for the features
                y_path: path for the labels
                X     : to take input features as array.
                y     : to take input labels as array.
                metric: Accepts values "mse", "rmse" or "mas" (Mean Squared Error,
                        Root Mean Squared Error and Mean absolute Error 
                        respectively). Determines how the model should be evaluated.

    Below is the *return* type.

    Returns
    -------
        float
            Metric value or score is returned.
    

    ``Note:`` Flexibilty of giving input to model in code is given as compared to 
    terminal. In code user can pass directly the numpy array for both features and labels.
    If both paths and arrays are given array overrides the path.
    """
    try:
        # read args
        parser = argparse.ArgumentParser(
            description="Take the model path, processed path and timestamp from the user."
        )
        add_mertic_arg(parser)
        add_model_pkl_file_path_arg(parser)
        add_x_path_arg(parser)
        add_y_path_arg(parser)
        add_logger_args(parser)
        args = parser.parse_args()
        show = True
        logger = loggerWrapper()

        if not model_pkl_file_path:
            show = False
            model_pkl_file_path = args.model_pkl_file_path
            logger = loggerWrapper(
                        args.log_level, args.log_path, args.no_console_log
                )

        if not model_pkl_file_path:
            raise Exception("Missing model pkl file path.")
        # get X, y
        X, y = [], []
        if args.X_path and args.y_path:
            X, y = load_csv(args.X_path), load_csv(args.y_path)

        elif kwargs.get("X", None) and kwargs.get("y", None):
            X, y = kwargs.get("X"), kwargs.get("y")
        elif kwargs.get("X_path") and kwargs.get("y_path"):
            X_path, y_path = kwargs.get("X_path"), kwargs.get("y_path")
            X, y = load_csv(X_path), load_csv(y_path)
        else:
            print("Missing file path for X and y")
            sys.exit(0)

        # get metric
        metric = "mse"
        if args.metric == "mse":
            if kwargs.get("metric", None):
                metric = kwargs.get("metric")
        else:
            metric = args.metric

        # load model
        logger.debug(f"Loading model from path {model_pkl_file_path} ....Starts")
        model = load_model_frm_pkl(model_pkl_file_path)
        logger.debug(f"Loading model from path {model_pkl_file_path} ....Done")
        y_pred = model.predict(X)
        # evaluate and return score
        
        score = get_score(metric, y, y_pred)
        logger.debug("Evaluation done.")
        if score:
            logger.debug(f"{metric.upper()}: {score}")

        if show:
            return score
    except Exception as e:
        logger.error(f"Error in evaluating.... {e}")
        return None
