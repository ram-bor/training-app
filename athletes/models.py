from django.db import models

# Create your models here.


class Athlete(models.Model):
    first_name = models.CharField(max_length=40,)
    last_name = models.CharField(max_length=40,)
    birth_date = models.DateField()
    threshold_hr = models.IntegerField()
    run_longest_distance = models.DecimalField(max_digits=5, decimal_places=2)


class Sport(models.Model):
    RUN = 'R'
    SWIM = 'S'
    BIKE = 'B'
    SPORT_CHOICES = [
        (RUN, 'Run'),
        (SWIM, 'Swim'),
        (BIKE, 'Bike')
    ]
    sport_type = models.CharField(
        max_length=32,
        choices=SPORT_CHOICES,
        default=RUN,
    )

    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    planned_duration = models.TimeField(blank=True, null=True)
    duration = models.TimeField()
    hour_avg = models.TimeField()
