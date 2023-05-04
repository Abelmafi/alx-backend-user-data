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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID:
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value:
        """
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(cookie_value)
        user = User.get(user_id)

        return user
