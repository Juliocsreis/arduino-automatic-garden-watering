from django.test import TestCase
from .models import Watering
from datetime import timedelta
from django.utils import timezone
from .api import viewsets
from django.urls import reverse


class WateringLogic(TestCase):

    def setUp(self):
        now = timezone.now()
        one_hour = now - timedelta(hours=1)
        pre_soil_humidity = 650
        after_soil_humidity = 400
        last_watering = Watering.objects.create(time_stamp=one_hour, pre_soil_humidity=pre_soil_humidity,
                                                after_soil_humidity=after_soil_humidity, watering_time_seconds=60)

        last_watering.save()
        self.last_watering = last_watering

    def test_check_soil_needs_watering_time(self):
        watering = viewsets.check_if_soil_needs_watering()
        self.assertEqual(watering, True)

    def test_post_dry_humidity_to_api(self):
        url = reverse('jardim_api:humidity')
        data = {'humidity': 900}
        response = self.client.post(url, data=data)
        watering = response.json()['watering']
        duration = response.json()['duration']
        print(response.status_code)
        print("watering", watering)
        print("duration", duration)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(watering, True)
        self.assertGreater(duration, 0)
