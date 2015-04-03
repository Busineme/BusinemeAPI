# -*- coding: utf-8 -*-

from importer.test.tests_basic import API_Test
import models


class API_Model(API_Test):

    """docstring for API_Model"""

    def test_model_instance(self):
        busline = models.BusLine()
        company = models.Company()

        self.assertIsNotNone(busline)
        self.assertIsNotNone(company)
