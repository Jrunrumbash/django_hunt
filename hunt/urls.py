from django.urls import path

from . import views

app_name = 'hunt'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:pk>/', views.TeamView.as_view(), name='team'),
    path('<int:pk>/clue/', views.Clue.as_view(), name='clue'),
    path('<str:team_name>/decrypt/', views.decrypt, name='decrypt'),
]
