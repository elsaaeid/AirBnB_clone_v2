#!/usr/bin/python3
""" Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class to create review object properties """
    text = ""
    user_id = ""
    place_id = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
