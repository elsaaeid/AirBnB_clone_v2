#!/usr/bin/python3
""" State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ class to create state object properties """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
