from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jardim.models import HumidityData, Watering
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST', ])
def humidity(self):
    no_data = -1
    if self.method == "POST":
        print('received post')
        soil_humidity = self.data.get('humidity', no_data)
        print("humidity", soil_humidity)
        if soil_humidity != no_data:
            interval, next_watering = check_last_watering_interval()
            watering = False
            duration = 0
            if interval:
                duration = watering_time_for_humidity(int(soil_humidity))
                save_humidity_data(soil_humidity)
                if duration:
                    watering = True
                    create_watering_obj(pre_humidity=soil_humidity, duration=duration)
            return Response(
                {"watering": watering, "duration": duration, "interval": interval, "next_watering": next_watering},
                status=status.HTTP_200_OK)
        else:
            return Response("No data received", status=status.HTTP_400_BAD_REQUEST)


def save_humidity_data(soil_humidity):
    humidity_data = HumidityData()
    humidity_data.humidity = soil_humidity
    humidity_data.save()


def watering_time_for_humidity(humidity):
    """return watering time in Seconds for each humidity"""
    if humidity > 800:
        return 600
    elif 600 < humidity < 800:
        return 240
    else:
        return False


def create_watering_obj(pre_humidity, duration):
    watering = Watering()
    watering.time_stamp = timezone.now()
    watering.pre_soil_humidity = pre_humidity
    watering.watering_time_seconds = duration
    watering.save()


def check_last_watering_interval():
    global last_watering
    try:
        last_watering = Watering.objects.latest('time_stamp')
    except ObjectDoesNotExist:
        time = timezone.now() - timedelta(minutes=21)
        last_watering = Watering.objects.create(time_stamp=time)
        last_watering.save()
    now = timezone.now()
    next_watering = last_watering.time_stamp + timedelta(minutes=20)
    next_watering_tz = next_watering - timedelta(hours=3)
    if now > next_watering:
        return True, next_watering_tz
    else:
        return False, next_watering_tz
