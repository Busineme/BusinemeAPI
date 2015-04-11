from tastypie.api import Api
from api.resources import BusLineResource, CompanyResource, TerminalResource

v1_api = Api(api_name='v1')
v1_api.register(CompanyResource())
v1_api.register(BusLineResource())
v1_api.register(TerminalResource())
