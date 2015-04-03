# -*- coding: utf-8 -*-

from importer.test.tests_basic import Parser_Test
from parser import Parser


class APP_Parser(Parser_Test):

    """docstring for APP_Parser"""

    def test_parser_instance(self):

        parser = Parser()
        self.assertIsNotNone(parser)
