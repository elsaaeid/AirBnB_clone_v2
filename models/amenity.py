#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)