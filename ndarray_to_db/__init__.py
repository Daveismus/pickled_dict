from ndarray_to_db.main import ndarrayDB


import sys
import logging

def easy_format():
    logging.basicConfig(
        format="%(funcName)s - %(levelname)s - line %(lineno)s - %(message)s",
        datefmt='%d-%m-%Y %H:%M:%S',
        level=logging.INFO
    )


if __name__ == '__main__':
    easy_format()
    ndarrayDB()