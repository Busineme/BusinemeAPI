# -*- coding: utf-8 -*-

from importer.test.tests_basic import API_Test
import models
import migrations
import views


class API_Model(API_Test):

    """docstring for API_Model"""

    def test_model_instance(self):
        busline = models.BusLine()
        company = models.Company()

        self.assertIsNotNone(busline)
        self.assertIsNotNone(company)


class API_Migration(API_Test):

    """docstring for API_Migration"""

    def test_migration_instance(self):

        self.assertIsNotNone(migrations)


class API_Views(API_Test):

    """docstring for API_Views"""

    def test_views_instance(self):

        self.assertIsNotNone(views)
