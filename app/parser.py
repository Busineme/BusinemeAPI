# -*- coding: utf-8 -*-

import csv
from api.models import BusLine


class Parser():

    def read_file(self, file_name):
        print "Opening csv file"
        csv_file = open(file_name)
        csv_file = csv.reader(csv_file, delimiter=',', quotechar="'")

        return csv_file

    def import_bus_lines(self):
        csv_file = self.read_file('app/data/bus_lines.csv')

        for row in csv_file:
            print 'Importing line: ', row[0]
            bus_line = BusLine()
            bus_line.line_number = row[0]
            bus_line.description = row[1]
            bus_line.fee = row[2]
            bus_line.route_size = row[3]
            bus_line.company = None
            bus_line.via = row[7]
            bus_line.save()
