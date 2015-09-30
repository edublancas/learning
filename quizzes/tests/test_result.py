#Test suite for quiz details
#Test suite for results details
#class ResultsTests(TestCase):
#   def test_route(self):

#Test for result saving
class SavingTests(TestCase):
    #Saving returns a confirmation message
    def test_save_result(self):
        c = Client()
        response = c.post('/quizzes/save/', {'name': 'test.md', 'score': 95})
        self.assertContains(response, text='Result saved.', count=1, status_code=200)
    #Saving actually saves ONE entry in db
    def test_save_one_record_to_db(self):
        c = Client()
        response = c.post('/quizzes/save/', {'name': 'test.md', 'score': 95.0})
        results = Result.objects.all()
        self.assertEqual(len(results), 1, 'No Result object saved')
    def test_save_info_to_db(self):
        c = Client()
        response = c.post('/quizzes/save/', {'name': 'test.md', 'score': 95.0})
        result = Result.objects.all()[0]
        self.assertEqual(result.name, 'test.md')
        self.assertEqual(result.score, 95.0)