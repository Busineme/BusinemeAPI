from django.db import models
from django.contrib.auth.models import User as DjangoUser
from api.exception import EmailAlreadyExistsError, UsernameAlreadyExistsError

# Create your models here.


class BusLine(models.Model):

    """docstring for BusLine"""

    line_number = models.CharField(max_length=5, unique=True)
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
    address = models.CharField(max_length=255, null=True,)

    def __unicode__(self):
        return self.description


class User(DjangoUser):
    pontuation = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id) + " - " + self.username

    def check_username(self):
        username_exists = User.objects.filter(username=self.username).count()
        if not username_exists:
            raise UsernameAlreadyExistsError()

    def check_email(self):
        email_exists = User.objects.filter(email=self.email).count()

        if not email_exists:
            raise EmailAlreadyExistsError()
