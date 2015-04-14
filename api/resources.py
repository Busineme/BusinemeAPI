from tastypie.resources import ModelResource
from tastypie import fields
from models import BusLine, Company, Terminal


class CompanyResource(ModelResource):

    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'


class TerminalResource(ModelResource):
    buslines = fields.ToManyField('api.resources.BusLineResource',
                                  'busline', null=True, full=True)

    class Meta:
        queryset = Terminal.objects.all()
        resource_name = 'terminal'


class BusLineResource(ModelResource):
    company = fields.ForeignKey(CompanyResource,
                                'company', null=True, full=True)
    terminals = fields.ToManyField(TerminalResource, full=True,
                                   attribute=lambda bundle: Terminal.objects.filter(busline=bundle.obj))

    class Meta:
        queryset = BusLine.objects.all()
        resource_name = 'busline'
