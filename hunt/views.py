from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Clue, Team, ClueState


class TeamView(generic.DetailView):
    model = Team
    template_name = 'hunt/team.html'


class Clue(generic.DetailView):
    model = Clue
    template_name = 'hunt/clue.html'


class IndexView(generic.ListView):
    template_name = 'hunt/index.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        return Team.objects.all()

def decrypt(request, team_name):
    team = get_object_or_404(Team, pk=team_name)
    try:
        selected_clue_set = team.cluestate_set.get(pk=request.POST['clue_id'])
        inserted_hash = request.POST['decrypt_code']
    except(KeyError, ClueState.DoesNotExist):
        return render(request, 'hunt/team.html', {
            'team' : team,
            'error_message': 'Failed to decrypt!',
        })
    else:
        clue = selected_clue_set.clue
        if clue.hash == inserted_hash:
            selected_clue_set.solved = True
            selected_clue_set.save()
        else:
            return render(request, 'hunt/team.html', {
                'team' : team,
                'error_message': 'Failed to decrypt!',
            })
    return HttpResponseRedirect(reverse('hunt:team', args=(team_name,)))
