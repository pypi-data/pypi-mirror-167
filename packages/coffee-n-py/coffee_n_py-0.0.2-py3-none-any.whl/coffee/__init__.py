"""A python utility for mimicing motion."""

import logging
import os

__version__ = "0.0.2"
APP_NAME: str = "coffee_n_py"

logging.basicConfig(
    format="%(asctime)s::%(module)s::%(filename)s::L%(lineno)d::%(levelname)s::%(message)s",
    filename=os.path.join(os.path.dirname(__file__), f"{APP_NAME}-app.log"),
    encoding="utf-8",
    level=logging.DEBUG,
    datefmt="%m/%d/%Y %H:%M:%S",
)
