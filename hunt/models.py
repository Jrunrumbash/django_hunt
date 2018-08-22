from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    creation_date = models.DateTimeField('date published')

    #TODO add a method for winning the game
    #def completed_the_game(self):


class Clue(models.Model):
    name = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    location_hint = models.CharField(max_length=200)

class Image(models.Model):
    clue = models.ForeignKey(Clue, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)


class ClueState(models.Model):
    clue = models.ForeignKey(Clue, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    solved = models.BooleanField()
