from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name+' score='+str(self.score)+' date='+str(self.date)