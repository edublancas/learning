from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, blank=True)