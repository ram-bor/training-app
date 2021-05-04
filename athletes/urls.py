from . import views
from django.urls import path, include


urlpatterns = [
    path('athletes/new', views.AthleteCreate.as_view(), name='athlete_create'),
    path('athlete_info', views.athlete_info, name='athlete_info'),
    path('training/new', views.TrainingCreate.as_view(), name='training_create'),

]
