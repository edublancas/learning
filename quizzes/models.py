from django.db import models

#Stores a reference to a deck
class Deck(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    def _get_last_done(self):
        q = Deck.objects.raw('SELECT id, date FROM quizzes_result WHERE deck_id=%s ORDER BY date DESC LIMIT 1', [self.id])
        try:
            return q[0].date
        except IndexError:
            return None
    def _get_last_score(self):
        q =  Deck.objects.raw('SELECT id, score FROM quizzes_result WHERE deck_id=%s ORDER BY date DESC LIMIT 1', [self.id])
        try:
            return q[0].score
        except IndexError:
            return None

    last_done = property(_get_last_done)
    last_score = property(_get_last_score)


#This model stores the score for a quiz
class Result(models.Model):
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    deck = models.ForeignKey(Deck)
    def __str__(self):
        return self.name+' score='+str(self.score)+' date='+str(self.date)

#This model creaters reminders for future quizzes for the user
class Reminder(models.Model):
    #Maybe this should be a foreign key to a Deck model
    deck_name = models.CharField(max_length=100)
    #Date when the quiz needs to be done
    date = models.DateTimeField(auto_now_add=True, blank=True)
    deck = models.ForeignKey(Deck)
