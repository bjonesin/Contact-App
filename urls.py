from django.conf.urls.defaults import *
from .views import contact_add
from .views import contact_list
from .views import contact_detail
from .views import my_view

urlpatterns = patterns('',
	url(r'^add/$', contact_add, name='contact-add'),
	url(r'detail/(?P<pk>\d+)?$', contact_detail, name= 'contact-detail'),
	url(r'^myview/$', my_view, name = 'my_view'),
	url(r'^list/$', contact_list, name='contact-list'),
	
	)