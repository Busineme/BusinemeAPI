from api.exception import EmailAlreadyExistsError, UsernameAlreadyExistsError
from django.db import IntegrityError
from models import BusLine, Company, Terminal, User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource, ALL


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

    def obj_create(self, bundle, **kwargs):
        bundle.obj.save()
        try:
            bundle = super(UserResource, self).obj_create(bundle, **kwargs)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.check_username()
            print 'OIUOIUOIU' * 80
            bundle.obj.check_email()
            bundle.obj.save()
        except UsernameAlreadyExistsError, error:
            return BadRequest({'code': 601, 'message': error})
        except EmailAlreadyExistsError, error:
            return BadRequest({'code': 602, 'message': error})
        except IntegrityError:
            return BadRequest()
