#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine import db_storage
    classes = db_storage.DBStorage.classes
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    classes = file_storage.FileStorage.classes
    storage = file_storage.FileStorage()
storage.reload()
