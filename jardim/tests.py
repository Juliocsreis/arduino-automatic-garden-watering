from django.test import TestCase
from .models import Watering
from datetime import timedelta
from django.utils import timezone
from .api import viewsets
from django.urls import reverse


class WateringLogic(TestCase):

    def test_check_soil_needs_watering_time(self):
        watering, next_interval = viewsets.check_last_watering_interval()
        print("next_interval", next_interval)
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

    def test_watering_under_interval(self):
        watering = Watering()
        watering.time_stamp = timezone.now()
        watering.save()
        url = reverse('jardim_api:humidity')
        data = {'humidity': 900}
        response = self.client.post(url, data=data)
        watering = response.json()['watering']
        duration = response.json()['duration']
        print(response.status_code)
        print("watering", watering)
        print("duration", duration)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(watering, False)
        self.assertEqual(duration, 0)

    def test_watering_above_interval(self):
        watering = Watering()
        time = timezone.now() - timedelta(minutes=21)
        watering.time_stamp = time
        watering.save()
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
