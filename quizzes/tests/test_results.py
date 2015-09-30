from django.test import TestCase
from django.test import Client

from ..models import Deck, Result

from datetime import datetime

class ResultsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create one deck 
        Deck(name='test_deck_1', filename='test_filename_1').save()
        #Create some results
        Result(score=100.0, deck_id=1, date=datetime(2015,01,01)).save()
        Result(score=99.0, deck_id=1, date=datetime(2015,01,02)).save()
        Result(score=98.0, deck_id=1, date=datetime(2015,01,03)).save()
        #Make the query to the route
        c = Client()
        cls.response = c.get('/quizzes/results/1/')
    #Test route works
    def test_route(self):
        self.assertEqual(ResultsTests.response.status_code, 200)
    #Test deck name appears
    def test_deck_name_appears(self):
        self.assertContains(ResultsTests.response, text='test_deck_1', count=1, status_code=200)
    #Test plot appears
    def test_plot_apperas(self):
        pass
    #Tests points in plot are correct
    def test_plot_correct(self):
        pass