# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, Client
from sys import stderr


class Basic_Tests(SimpleTestCase):

    """Basic test class"""
    name = ''
    my_type = ''

    def getName(self):
        """ Get the name of the test """
        self.name = str(self.id).split('=')[-1][:-2]
        self.name = self.name.split('test_')[-1]
        self.name = self.name.replace('_', ' ')

    def __str__(self):
        self.getName()
        out = '\r%s %s test ' % (self.my_type, self.name)
        out = out.ljust(70, '-')
        return out

    def tearDown(self):
        stderr.write(' Done\n')

    def shortDescription(self):
        return "Teste da classe %s" % self.__class__.__name__


class Validate_Test(Basic_Tests):

    """Basic test class to Validations"""

    def setUp(self):
        self.my_type = '[Validation]'
        stderr.write(self.__str__())
        self.shortDescription()


class API_Test(Basic_Tests):

    """Basic test class to API"""

    def setUp(self):
        self.my_type = '[API]'
        stderr.write(self.__str__())
        self.shortDescription()


class Parser_Test(Basic_Tests):

    """Basic test class to Parser"""

    def setUp(self):
        self.my_type = '[Parser]'
        stderr.write(self.__str__())
        self.shortDescription()
