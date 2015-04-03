from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from api.rest_api import BusLineResource, CompanyResource

v1_api = Api(api_name='v1')
v1_api.register(CompanyResource())
v1_api.register(BusLineResource())

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'BusinemeAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
