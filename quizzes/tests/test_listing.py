from django.test import TestCase
from django.test import Client

from ..decks import list_decks
from ..models import Deck, Result

from datetime import datetime

#Test suite for quizz listing
class ListingTests(TestCase):
    #Create 10 decks and make a request to the route
    @classmethod
    def setUpTestData(cls):
        #Create some decks
        Deck(name='test_deck_1', filename='test_filename_1').save()
        Deck(name='test_deck_2', filename='test_filename_2').save()
        Deck(name='test_deck_3', filename='test_filename_3').save()
        Deck(name='test_deck_4', filename='test_filename_4').save()
        Deck(name='test_deck_5', filename='test_filename_5').save()
        Deck(name='test_deck_6', filename='test_filename_6').save()
        Deck(name='test_deck_7', filename='test_filename_7').save()
        Deck(name='test_deck_8', filename='test_filename_8').save()
        Deck(name='test_deck_9', filename='test_filename_9').save()
        #Create some fake results
        #Many for one deck
        Result(score=100.0, deck_id=1, date=datetime(2015,01,01)).save()
        Result(score=99.0, deck_id=1, date=datetime(2015,01,02)).save()
        Result(score=98.0, deck_id=1, date=datetime(2015,01,03)).save()
        #Just one for deck 2
        Result(score=97.0, deck_id=2, date=datetime(2015,01,04)).save()

        c = Client()
        cls.response = c.get('/quizzes/list/')
    #Test route works
    def test_route(self):
        self.assertEqual(ListingTests.response.status_code, 200)
    #Test listing shows all decks
    def test_list(self):
        self.assertContains(ListingTests.response, text='test_deck_1', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_2', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_3', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_4', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_5', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_6', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_7', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_8', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='test_deck_9', count=1, status_code=200)
    #Test button to start quiz
    def test_start_quiz_button(self):
        self.assertContains(ListingTests.response, text='/quizzes/detail/1', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/2', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/3', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/4', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/5', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/6', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/7', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/8', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/detail/9', count=1, status_code=200)
    #Test button to review results appears
    def test_review_results_button(self):
        self.assertContains(ListingTests.response, text='/quizzes/results/1', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/2', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/3', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/4', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/5', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/6', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/7', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/8', count=1, status_code=200)
        self.assertContains(ListingTests.response, text='/quizzes/results/9', count=1, status_code=200)
    #Test button to add new deck appears
    def test_new_deck_button_visible(self):
        self.assertContains(ListingTests.response, text='Add new deck', count=1, status_code=200)
    #Test last done date is correct
    def test_last_done(self):
        #This is last date for deck one
        self.assertContains(ListingTests.response, text='2015-01-03', count=1, status_code=200)
        #This is last date for deck two
        self.assertContains(ListingTests.response, text='2015-01-04', count=1, status_code=200)
    #Test last score is correct
    def test_last_score(self):
        #Last score for deck 1
        self.assertContains(ListingTests.response, text='98', count=1, status_code=200)
        #Lasr score for deck 2
        self.assertContains(ListingTests.response, text='97', count=1, status_code=200)