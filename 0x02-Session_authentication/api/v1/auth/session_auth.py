#!/usr/bin/env python3
""" Defination of class SessionAuth. """
from .auth import Auth


class SessionAuth(Auth):
    """
    A subclass of Auth that provides session-based authentication.
    It can be used in conjunction with a web framework to authenticate users
    and restrict access to certain routes or resources.
    
    """
    pass
