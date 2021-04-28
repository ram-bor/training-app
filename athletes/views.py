from django.views import View
from django.shortcuts import render, redirect
from .models import Athlete, Training
from .forms import AthleteForm
from rest_framework import generics
from .serializers import AthleteSerializer


# Create your views here.

class AthleteCreate(View):
    form_class = AthleteForm
    template_name = 'athletes/athlete_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            athlete = form.save()
            return redirect('athlete_info', pk=athlete.pk)

        return render(request, self.template_name, {'form': form})


class AthleteInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    # permissions_classes = (permissions.IsAuthenticated)
