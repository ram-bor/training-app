from django.views import View
from django.shortcuts import render, redirect
from .models import Athlete, Training
from .forms import AthleteForm


# Create your views here.

# class AthleteCreate(View):

#     def get(self, request):
#         athlete_form = AthleteForm()
#         return render(request, 'athlete_form.html')

#     def post(self, request):
#         athlete_form = AthleteForm(request.POST)
#         if athlete_form.is_valid():
#             athlete = athlete_form.save()
#             return redirect('athlete_detail', pk=athlete.pk)

#         return render(request, 'athlete_form.html')

class AthleteInfo(view):
    def get(self, request):
        athlete =
