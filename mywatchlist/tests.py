from django.test import TestCase, Client
from django.urls import resolve
from mywatchlist.views import MyWatchList

# Create your tests here.

class MyWatchListTest(TestCase):
    def test_mywatchlist_url_is_exist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml_url_is_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_json_url_is_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    