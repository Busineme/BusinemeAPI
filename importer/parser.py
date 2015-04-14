# -*- coding: utf-8 -*-

import csv
from api.models import BusLine, Terminal, Company


class Parser(object):

    def read_file(self, file_name):
        csv_file = open(file_name)
        csv_file = csv.reader(csv_file, delimiter=',', quotechar="'")

        return csv_file

    def import_bus_lines(self):
        csv_file = self.read_file('importer/data/bus_lines.csv')

        print 'Importing BusLines...'
        for row in csv_file:
            bus_line = BusLine()
            bus_line.line_number = row[0]
            bus_line.description = row[1]
            bus_line.fee = row[2]
            bus_line.route_size = row[3]
            bus_line.company = None
            bus_line.via = row[7]
            bus_line.save()

    def import_terminals(self):
        csv_file = self.read_file('importer/data/terminals.csv')

        print 'Importing Terminals...'
        for row in csv_file:
            terminal = Terminal()
            terminal.description = row[0]
            terminal.save()

    def import_companies(self):
        csv_file = self.read_file('importer/data/companies.csv')

        print 'Importing Companies...'
        for row in csv_file:
            company = Company()
            company.name = row[0]
            company.save()
