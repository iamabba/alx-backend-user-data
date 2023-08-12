#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar
from flask import request, jsonify, abort

class BasicAuth(Auth):
    """ Basic Authentication Class """

    # ... (the rest of your existing code)

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user

from api.v1.views.users import User
from flask import request, jsonify

@app.before_request
def before_request():
    """ Run before every request """
    if auth.require_auth(request.path, ['/api/v1/status/',
                                        '/api/v1/unauthorized/',
                                        '/api/v1/forbidden/']):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)
        request.current_user = auth.current_user(request)

@app.route('/users/me', methods=['GET'], strict_slashes=False)
def get_current_user():
    """ Retrieves the authenticated User """
    user = request.current_user
    return jsonify(user.to_json()), 200