from django.conf.urls import url

from . import views

app_name = 'TemperatureController'
urlpatterns = [
    url(r'^$', views.sensors, name='sensors'),
    url(r'^details/(?P<sensor_id>[0-99]+)/$', views.detail, name='detail'),
    url(r'^disable/(?P<sensor_id>[0-99]+)/$', views.disable, name='disable'),
]