from . import views
from django.urls import path, include


urlpatterns = [
    path('athlete/signup', views.AthleteCreate, name='athlete_create'),
]
