from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^(?P<robot_id>[0-9]+)/$', views.direction, name='direction'),
	url(r'^power_off/$', views.power_off, name='power_off'),
]
