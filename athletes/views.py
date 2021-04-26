from django.shortcuts import render
from .forms import UserForm

# Create your views here.


def create_athlete(request):
    athlete_form = UserForm()
    return render(request, 'my_template.html', {'my_form': athlete_form})
