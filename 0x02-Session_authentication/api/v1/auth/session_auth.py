#!/usr/bin/env python3
""" Defination of class SessionAuth. """
from .auth import Auth
import uuid

class SessionAuth(Auth):
    """
    A subclass of Auth that provides session-based authentication.
    It can be used in conjunction with a web framework to authenticate users
    and restrict access to certain routes or resources.
    
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a user ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
