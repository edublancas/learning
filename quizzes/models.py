from django.db import models

#This model stores the score for a quiz
class Result(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name+' score='+str(self.score)+' date='+str(self.date)

#This model creaters reminders for future quizzes for the user
class Reminder(models.Model):
    #Maybe this should be a foreign key to a Deck model
    deck_name = models.CharField(max_length=100)
    #Date when the quiz needs to be done
    date = models.DateTimeField(auto_now_add=True, blank=True)
