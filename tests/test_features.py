import requests
import lxml.html
from django.test import TestCase

from webcred import features


class FeatureTest(TestCase):

    def setUp(self):
        url = 'https://www.example.com'
        response = requests.get(url)
        document = lxml.html.fromstring(response.text)

        self.data = {
            'url': response.url,
            'res': response,
            'doc': document
        }

        self.store = {}

    def test_advertisements(self):
        features.advertisements(self.data, self.store)
        self.assertEqual(self.store['advertisements'], 0)

    def test_broken_links(self):
        features.broken_links(self.data, self.store)
        self.assertEqual(self.store['broken_links'], 0)

    def test_internationalization(self):
        features.internationalization(self.data, self.store)
        self.assertEqual(self.store['internationalization'], 0)

    def test_internet_domain(self):
        features.internet_domain(self.data, self.store)
        self.assertEqual(self.store['internet_domain'], 'com')
