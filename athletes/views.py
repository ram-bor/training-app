from django.shortcuts import render
from .forms import UserForm
from django.views import View

# Create your views here.


class AthleteCreate(View):
    def create_athlete(request):
        athlete_form = UserForm()
        return render(request, 'athlete_form.html', {'my_form': athlete_form})
