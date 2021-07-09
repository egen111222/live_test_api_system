from django.db import models

class Note(models.Model):
    number_user = models.IntegerField()
    coins = models.IntegerField()
    goods = models.IntegerField()


class Event(models.Model):
    name = models.CharField(max_length=50)
    place = models.IntegerField()
    
