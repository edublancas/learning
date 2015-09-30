from django.test import TestCase
from django.test import Client

from ..decks import list_decks
from ..models import Result

#Test suite for quizz listing
class ListingTests(TestCase):
    #Test route answers with 200
    def test_route(self):
        c = Client()
        response = c.get('/quizzes/list/')
        self.assertEqual(response.status_code, 200)
    #Test webpage shows al files in decks folder
    #links to start and links to see results
    def test_listing(self):
        c = Client()
        response = c.get('/quizzes/list/')
        decks = list_decks()
        for deck in decks:
            self.assertContains(response, text=deck, count=3, status_code=200)