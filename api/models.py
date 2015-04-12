from django.db import models

# Create your models here.


class BusLine(models.Model):

    """docstring for BusLine"""

    line_number = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.FloatField()  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    def __unicode__(self):
        return self.line_number + " - " + self.description


class Company(models.Model):

    """docstring for Company"""

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Terminal(models.Model):

    """docstring for Terminal"""

    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
