from . import views
from django.urls import path, include


urlpatterns = [
    path('athlete/new', views.AthleteCreate.as_view(), name='athlete_create'),
    path('athlete/<int:pk>', views.AthleteInfo.as_view()),
    path('training/new', views.TrainingCreate.as_view(), name='training_create'),

]
