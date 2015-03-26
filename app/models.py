from django.db import models

# Create your models here.


class BusLine(models.Model):
    """docstring for BusLine"""

    line_number = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()
    fee = models.FloatField()
    company = models.ForeignKey('Company', null=True)

class Company(models.Model):
    """docstring for Company"""

    name = models.CharField(max_length=255)