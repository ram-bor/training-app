from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.AthleteCreate.as_view(), name='athlete_create'),
]
