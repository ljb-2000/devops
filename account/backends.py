#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .models import User


class AuthBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        if username is None:
            username = User.USERNAME_FIELD
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

