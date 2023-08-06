import logging
import sys
from pathlib import Path
import os


def get_package_name():
    return os.path.basename(str(Path(__file__).parents[1]))


def info(message: str):
    return logging.getLogger(get_package_name()).info(message)


def warning(message: str):
    return logging.getLogger(get_package_name()).warning(message)


def debug(message: str):
    return logging.getLogger(get_package_name()).debug(message)


def error(message: str):
    return logging.getLogger(get_package_name()).error(message)


def exception(message: str):
    return logging.getLogger(get_package_name()).exception(message)


def log(message: str):
    return logging.getLogger(get_package_name()).log(message)


def critical(message: str):
    return logging.getLogger(get_package_name()).critical(message)
