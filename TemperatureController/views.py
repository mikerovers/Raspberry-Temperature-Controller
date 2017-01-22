from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from TemperatureController.models import Sensor

def sensors(request):
    latest_sensor_list = Sensor.objects.all()
    context = {
        'latest_sensor_list': latest_sensor_list,
    }

    return render(request, 'TemperatureController/sensors.html', context)

def detail(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    context = {
        'sensor' : sensor,
    }
    return render(request, 'TemperatureController/detail.html', context)

def disable(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    sensor.enabled = not sensor.get_enabled()
    sensor.save()

    latest_sensor_list = Sensor.objects.all()

    context = {
        'latest_sensor_list': latest_sensor_list,
    }

    return render(request, 'TemperatureController/sensors.html', context)