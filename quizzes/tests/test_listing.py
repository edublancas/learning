from django.test import TestCase
from django.test import Client

from ..decks import list_decks
from ..models import Result, Deck

from django.conf import settings

#Test suite for quizz listing
class ListingTests(TestCase):
    #Make request to the route
    def setUp(self):
        d = Deck(name='test_deck_1', filename='test_deck_filename_1')
        d.save()
        c = Client()
        self.response = c.get('/quizzes/list/')
    #Test route works
    def test_route(self):
        self.assertEqual(self.response.status_code, 200)
    #Test listing shows all decks
    def test_list(self):
        print settings.DATABASES['default']
        print Deck.objects.all()
        print self.response.content
        self.assertContains(self.response, text='test_deck_1', count=1, status_code=200)
        #self.assertContains(self.response, text='test_deck_2', count=1, status_code=200)
    #Test button to start quiz appears
    #Test button to review results appears
    #Test button to add new deck appears
    #Test last done date is correct
    #Test last score is correct