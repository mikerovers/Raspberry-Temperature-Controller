from django.db import models
import TemperatureController.TempCore

# Create your models here.
class Sensor(models.Model):
    sensor_description = models.CharField(max_length=50)
    sensor_id = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def get_description(self):
        return self.sensor_description

    def get_sensor_id(self):
        return self.sensor_id

    def get_temperature(self):
        return TemperatureController.TempCore.read_temp_raw(self.get_sensor_id())

    def get_enabled(self):
        return self.enabled
