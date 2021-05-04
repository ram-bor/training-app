from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Athlete, Training
from .forms import AthleteForm, TrainingForm
from rest_framework import generics, permissions
from .serializers import AthleteSerializer
from django.urls import reverse_lazy


# Create your views here.

class AthleteCreate(View):
    form_class = AthleteForm
    template_name = 'athlete_form.html'

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
    permissions_classes = (permissions.IsAuthenticated)


# def athlete_info(request, pk):
#     athlete = Athlete.objects.get(pk=pk)
#     return render(request, 'athletes/athlete_info.html', {'athlete': athlete})


class TrainingCreate(View):
    form_class = TrainingForm
    template_name = 'training_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            training = form.save()
            return redirect('training_info', pk=training.pk)

        return render(request, self.template_name, {'form': form})


# class TrainingDetail
