from tastypie.resources import ModelResource, ALL
from tastypie import fields
from tastypie.authorization import Authorization
from models import BusLine, Company, Terminal, User


class CompanyResource(ModelResource):

    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'


class TerminalResource(ModelResource):

    class Meta:
        queryset = Terminal.objects.all()
        resource_name = 'terminal'
        filtering = {
            'description': ('exact', 'startswith', 'contains')
        }


class BusLineResource(ModelResource):
    company = fields.ForeignKey(CompanyResource,
                                'company', null=True, full=True)
    terminals = fields.ToManyField(
        TerminalResource, full=True,
        attribute=lambda bundle: Terminal.objects.filter(busline=bundle.obj))

    class Meta:
        queryset = BusLine.objects.all()
        resource_name = 'busline'
        filtering = {
            'line_number': ('contains'),
            'description': ('contains')
        }


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.filter(is_active=True)
        resource_name = 'user'
        authorization = Authorization()
        excludes = ['is_active', 'is_staff', 'is_superuser', 'last_name',
                    'password', 'last_login', ]
        filtering = {
            'username': ALL
        }
