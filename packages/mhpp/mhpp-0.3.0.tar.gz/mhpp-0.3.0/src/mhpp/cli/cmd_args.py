import os
import pathlib
import argparse
from mhpp.config import DefaultConfig

"""This module helps to take cli args from user.
The function name itself describes its functionality.
"""
CONFIG = DefaultConfig()


def add_data_path_arg(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "-dp", 
        "--data-path",
        help="To take input path from user to download the fetched data.",
        type=pathlib.Path,
        default=CONFIG.DATA_RAW_PATH,
    )

    
def add_processed_path_arg(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "-pp",
        "--processed-path",
        help="To take input path from user to save the processed data",
        type=pathlib.Path,
        default=CONFIG.DATA_PROCESSED_PATH,
    )

def add_train_test_data_path_arg(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "-ttp", 
        "--train-test-data-path",
        help="To take output data path for saving the train and test data.",
        type=pathlib.Path,
        default=CONFIG.TRAIN_TEST_DATA,
    )

def add_mertic_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-m",
        "--metric",
        help="To take input metric from the user to evaluate the model.",
        # nargs=1,
        default="rmse",
        choices=["mse", "rmse", "mas", "all"],
    )


def add_pkl_path_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-pkl",
        "--pickel-path",
        help="To take input directory from user to save the model pickel file.",
        type=pathlib.Path,
        default=CONFIG.MODELS_PATH,
    )

def add_model_pkl_file_path_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-mpkl",
        "--model-pkl-file-path",
        help="To take input from the user for reading the model pickel file path.",
        type=pathlib.Path,
        default=None,
    )


def add_x_path_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-x",
        "--X-path",
        help="To take input from the user for X or features.",
        type=pathlib.Path,
        default=None,
    )


def add_y_path_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-y", "--y-path", 
        help="To take input from the user for y or labels.", 
        type=pathlib.Path,
        default=None
    )


def add_model_name_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-mn",
        "--model-name",
        help="To take input from the user for model name.",
        default="latest",
    )


def add_algo_name_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-an",
        "--algo-name",
        help="To take input from the user for algo name.",
        default="lr",
        choices=["lr", "dtr", "rfr"],
    )

def add_logger_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "-ll", 
        "--log-level",
        help="To take input from user for specific log level.",
        type=str,
        default="DEBUG",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    parser.add_argument(
        "-lp", 
        "--log-path",
        help="To take input from user for log path to save logs.",
        type=pathlib.Path,
        default=None,
    )
    parser.add_argument(
        "-ncl", 
        "--no-console-log",
        help="To take input from user for setting console log.",
        action = "store_true",
        default = False
    )
