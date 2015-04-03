from tastypie.resources import ModelResource
from tastypie import fields
from models import BusLine, Company

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'
        fields = ['name']
        include_resource_uri = False

class BusLineResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company', null = True, full = True)
    class Meta:
        queryset = BusLine.objects.all()
        resource_name = 'bus_line'
        excludes = ['id', 'via']
        include_resource_uri = False
