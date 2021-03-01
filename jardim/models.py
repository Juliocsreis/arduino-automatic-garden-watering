from django.db import models


class HumidityData(models.Model):
    time_stamp = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    humidity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Watering(models.Model):
    time_stamp = models.DateTimeField(null=True, blank=True, auto_now_add=False)
    pre_soil_humidity = models.IntegerField(null=True, blank=True)
    after_soil_humidity = models.IntegerField(null=True, blank=True)
    watering_time_seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)