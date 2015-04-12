# -*- coding: utf-8 -*-

from configuration.tests import APITest
from api import models


class TestModels(APITest):

    """docstring for API_Model"""

    def test_model_instance(self):
        busline = models.BusLine()
        company = models.Company()

        self.assertIsNotNone(busline)
        self.assertIsNotNone(company)
        self.assertIsNotNone(company.__unicode__())
        self.assertIsNotNone(busline.__unicode__())
