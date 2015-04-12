# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from sys import stderr

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=api,importer',
    '--cover-erase',
    '--exe',
    '--with-doctest',
    '--all-modules',
    '--logging-clear-handlers',
    '-d',  # Add detail to error output
    # '--cover-html',
    # '-s',  # print stdout
    '--cover-tests',  # test tests
    '--nologcapture',
    '--verbosity=2',
]


class BusinemeTests(SimpleTestCase):

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
        return out + ' '

    def tearDown(self):
        # stderr.write(' Done\n')
        pass

    def shortDescription(self):
        return "Teste da classe %s" % self.__class__.__name__

    def setUp(self):
        stderr.write(self.__str__())
        self.shortDescription()


class APITest(BusinemeTests):

    """Basic test class to API"""

    my_type = '[API]'


class ParserTest(BusinemeTests):

    """Basic test class to Parser"""

    my_type = '[Parser]'
