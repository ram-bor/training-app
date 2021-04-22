from django.db import models

# Create your models here.


class Athlete(models.Model):
    first_name = models.CharField(max_length=40,)
    last_name = models.CharField(max_length=40,)


class Workout(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, related_name='workouts')
