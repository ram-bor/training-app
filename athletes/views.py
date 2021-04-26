from django.views import View
from django.shortcuts import render, redirect
# from .forms import UserForm
# from .forms import AthleteForm

# Create your views here.


class AthleteCreate(View):

    def get(self, request):
        athlete_form = UserForm()
        return render(request, 'athlete_form.html', {'form': athlete_form})

    def post(self, request):
        athlete_form = UserForm(request.POST)
        if athlete_form.is_valid():
            athlete = athlete_form.save()
            return redirect('athlete_detail', pk=athlete.pk)

        return render(request, 'athlete_form.html', {'form': athlete_form})
