from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class SubscriptionListTestCase(APITestCase):

    def test_create_subscription(self):
        url = reverse('subscription-list')
        data = {
            'name': 'Netflix',
            'description': 'Moovies',
            'currency': 'EUR',
            'amount': 10,
            'first_billing_date': '12/03/2019',
            'billing_cycle': 'Monthly'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SubscriptionDetailTestCase(APITestCase):
    pass