# -*- coding: utf-8 -*-

from configuration.tests import APITest
from api import models


class TestModels(APITest):

    """docstring for API_Model"""

    def test_model_package(self):
        self.assertIsNotNone(models)

    def test_model_instance(self):
        company = models.Company(name='Marechal')
        company.save()

        busline = models.BusLine(line_number='0.205',
                                 description='Taguatinga - Gama',
                                 via='M. Norte',
                                 route_size=42.0,
                                 fee=3.0,
                                 company=company)
        busline.save()

        self.assertIsNotNone(busline)
        self.assertIsNotNone(busline.__unicode__())
        self.assertIsNotNone(company)
        self.assertIsNotNone(company.__unicode__())

    def test_model_terminal(self):
        terminal = models.Terminal()
        self.assertIsNotNone(terminal)
