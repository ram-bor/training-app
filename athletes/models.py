from django.db import models

# Create your models here.


class Athlete(models.Model):
    first_name = models.CharField(max_length=40,)
    last_name = models.CharField(max_length=40,)
    birth_date = models.DateField()
    threshold_hr = models.IntegerField()
    run_longest_distance = models.DecimalField(max_digits=5, decimal_places=2)


class Workout(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
