# -*- coding: utf-8 -*-

from importer.test.tests_basic import Parser_Test
from parser import Parser


class APP_Parser(Parser_Test):

    """docstring for APP_Parser"""

    def test_parser_instance(self):

        parser = Parser()
        self.assertIsNotNone(parser)

    def test_parser_read_file(self):

        parser = Parser()
        print ''
        self.assertRaises(IOError, parser.read_file, '')
        self.assertRaises(IOError, parser.read_file, 'away')
        file = 'importer/data/bus_lines.csv'
        self.assertIsNotNone(parser.read_file(file))