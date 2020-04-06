import numpy as np
import sqlite3 as sql
import logging
from typing import *

from os import PathLike
from numpy import ndarray


class ndarrayDB:
    def __init__(self, db: PathLike):  # if it has a
        self.db = db
        self.conn = None
        self.c = None
        self._connect()

    def load_data(self, name):
        ...

    def save_data(self, array: ndarray, loc: str):
        self._check_table(loc)
        array = list(array)
        self.c.executemany(f"""insert into {loc}
            """)

    def _connect(self):
        """
        connects to the selected database and if it doesnt exist it will be created
        :return:
        """
        self.conn = sql.connect(self.db)
        self.c = self.conn.cursor()

    def end(self):
        """
        ends the connection
        :return:
        """
        self.conn.close()

    def _check_table(self, name: str):
        """
        it checks if the table exists and if not it creates it
        :param name:
        :return:
        """
