from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Card, IPO

class CardAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.card_data = {
            'name': 'Test Card',
            'description': 'This is a test card',
        }
        self.card = Card.objects.create(**self.card_data)

    def test_get_all_cards(self):
        response = self.client.get('/api/cards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_card(self):
        response = self.client.get(f'/api/cards/{self.card.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.card.name)

    def test_create_card(self):
        new_card = {
            'name': 'Another Card',
            'description': 'Another description'
        }
        response = self.client.post('/api/cards/', new_card, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 2)

class IPOAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ipo_data = {
            'company_name': 'Bluestock Fintech',
            'price_band': '100-120',
            'issue_size': '₹100 Cr',
            'status': 'Open'
        }
        self.ipo = IPO.objects.create(**self.ipo_data)

    def test_get_all_ipos(self):
        response = self.client.get('/api/ipo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_ipo(self):
        response = self.client.get(f'/api/ipo/{self.ipo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], self.ipo.company_name)

    def test_create_ipo(self):
        new_ipo = {
            'company_name': 'Test Ltd.',
            'price_band': '200-250',
            'issue_size': '₹50 Cr',
            'status': 'Upcoming'
        }
        response = self.client.post('/api/ipo/', new_ipo, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IPO.objects.count(), 2)
