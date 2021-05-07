from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .serializers import AthleteSerializer, TrainingSerializer
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Athlete, Training
from .forms import AthleteForm, TrainingForm
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


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


# class AthleteInfo(generics.RetrieveUpdateDestroyAPIView):

    # queryset = Athlete.objects.get(pk=pk)
    # serializer_class = AthleteSerializer
    # permissions_classes = (permissions.IsAuthenticated)

class AthleteInfo(APIView):
    # template_name = 'athlete_info.html'

    def get_athlete(self, pk):
        try:
            return Athlete.objects.get(pk=pk)
        except Athlete.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        athlete = self.get_athlete(pk)
        serializer = AthleteSerializer(athlete)
        return Response(serializer.data)


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
