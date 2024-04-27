#!/usr/bin/python3

"""Initializes the file in models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
