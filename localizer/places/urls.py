
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^navbar/$', views.navbar_info, name='navbar_info'),
	url(r'^search/$', views.search, name='search'),
	url(r'^content/(?P<type>\w+)/(?P<location>\w+)/$', views.content, name='content'),
	url(r'^item/(?P<place_id>[\w\+\_\-])/$', views.item, name='item'),
]