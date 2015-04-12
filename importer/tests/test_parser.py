# -*- coding: utf-8 -*-

from configuration.tests import ParserTest
from importer.parser import Parser


class TestParser(ParserTest):

    """docstring for API_Views"""

    def test_parser(self):

        self.assertTrue(True)

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

    def test_parser_import_bus_lines(self):
        parser = Parser()
        print ''
        self.assertIsNone(parser.import_bus_lines())
