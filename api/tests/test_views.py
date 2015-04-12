# -*- coding: utf-8 -*-

from configuration.tests import APITest
from api import views


class TestViews(APITest):

    """docstring for API_Views"""

    def test_views_instance(self):

        self.assertIsNotNone(views)
