from django.db import models


class esp8266Test(models.Model):
    time_stamp = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    info = models.CharField(null=True, blank=True, max_length=250)

    def __str__(self):
        return str(self.pk)