#!/usr/bin/python3
""" User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ class to create user object properties """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
