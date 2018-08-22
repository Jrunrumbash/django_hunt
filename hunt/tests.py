from django.test import TestCase
from django.utils import timezone
from hashlib import sha224
from django.urls import reverse

from .models import Clue, ClueState, Team

# Create your tests here.

def createClue(name, location_hint):
    hash = sha224(name.encode('utf-8')).hexdigest()
    return Clue.objects.create(name=name, location_hint=location_hint, hash=hash)

def createTeam(name):
    time = timezone.now()
    return Team.objects.create(name=name, creation_date=time)


class ClueViewTest(TestCase):


class TeamViewTest(TestCase):
    def test_add_clue_to_team(self):
        clue = createClue('testClue', 'I am here')
        team = createTeam('test_team')
        ClueState.objects.create(team=team, clue=clue ,solved=False)

        response = self.client.get(reverse('hunt:team', args=(team.name,)))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, clue.hash)

    def test_solve_clue_shows_name(self):
        clue = createClue('testClue', 'I am here')
        team = createTeam('test_team')
        ClueState.objects.create(team=team, clue=clue ,solved=True)

        response = self.client.get(reverse('hunt:team', args=(team.name,)))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, clue.name)

    def test_

