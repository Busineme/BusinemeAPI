# -*- coding: utf-8 -*-

from configuration.tests import APITest
from api import resources


class TestResources(APITest):

    """docstring for Rest_API"""

    def test_resource_api_instance(self):
        company_resource = resources.CompanyResource()
        busline_resource = resources.BusLineResource()

        self.assertIsNotNone(company_resource)
        self.assertIsNotNone(busline_resource)
