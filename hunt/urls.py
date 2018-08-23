from django.urls import path

from . import views

app_name = 'hunt'
urlpatterns = [
    path('', views.register, name='index'),
    path('team/<str:pk>/', views.TeamView.as_view(), name='team'),
    path('<int:pk>/clue/', views.ClueView.as_view(), name='clue'),
    path('<str:team_name>/decrypt/', views.decrypt, name='decrypt'),
    path('register', views.register, name="register"),
]
