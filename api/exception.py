# -*- coding: utf-8 -*-


class EmailAlreadyExistsError(Exception):

    def __str__(self):
        return 'Email already registered.'


class UsernameAlreadyExistsError(Exception):

    def __str__(self):
        return 'Username already registered.'
