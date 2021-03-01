from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jardim.models import HumidityData, Watering
from datetime import timedelta
from django.utils import timezone


@api_view(['POST', ])
def humidity(self):
    no_data = 0
    if self.method == "POST":
        print('received post')
        soil_humidity = self.data.get('humidity', no_data)
        print("humidity", soil_humidity)
        duration = 0
        if soil_humidity != no_data:
            test = HumidityData()
            test.humidity = soil_humidity
            test.save()
            watering = check_if_soil_needs_watering()
            if watering:
                duration = watering_time_for_humidity(int(soil_humidity))
            return Response({"watering": watering, "duration": duration}, status=status.HTTP_200_OK)
        else:
            return Response()


def watering_time_for_humidity(humidity):
    """return watering time in Seconds for each humidity"""
    if humidity > 800:
        return 600
    elif 600 < humidity < 800:
        return 240
    else:
        return False


def check_if_soil_needs_watering():
    last_watering = Watering.objects.latest('time_stamp')
    now = timezone.now()
    next_watering = now + timedelta(minutes=20)
    if next_watering > last_watering.time_stamp:
        return True
    else:
        return False


