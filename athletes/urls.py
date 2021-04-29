from . import views
from django.urls import path, include


urlpatterns = [
    path('athletes/new', views.AthleteCreate.as_view(), name='athlete_create'),
    path('athlete_info', views.AthleteInfo.as_view(), name='athlete_info'),
]
