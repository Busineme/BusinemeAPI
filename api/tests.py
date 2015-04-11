# -*- coding: utf-8 -*-

from importer.test.tests_basic import API_Test
import models
import migrations
import views
import rest_api


class API_Model(API_Test):

    """docstring for API_Model"""

    def test_model_instance(self):
        busline = models.BusLine()
        company = models.Company()

        self.assertIsNotNone(busline)
        self.assertIsNotNone(company)
        self.assertIsNotNone(company.__unicode__())
        self.assertIsNotNone(busline.__unicode__())


class API_Migration(API_Test):

    """docstring for API_Migration"""

    def test_migration_instance(self):

        self.assertIsNotNone(migrations)
        print migrations.__dict__['__package__']


class API_Views(API_Test):

    """docstring for API_Views"""

    def test_views_instance(self):

        self.assertIsNotNone(views)


class API_Rest(API_Test):

    """docstring for Rest_API"""

    def test_resource_api_instance(self):
        CompanyResource = rest_api.CompanyResource()
        BusLineResource = rest_api.BusLineResource()

        self.assertIsNotNone(CompanyResource)
        self.assertIsNotNone(BusLineResource)
