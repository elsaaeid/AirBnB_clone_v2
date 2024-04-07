#!/usr/bin/python3

"""amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
