#!/usr/bin/env python3

# BoBoBo

from sqlite3 import dbapi2

import boon.db.database as database


def get_db(conf):
    return database.get_db(conf, dbapi2)
