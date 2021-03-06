from django.db import models
from django.urls import reverse

# Create your models here.


class Athlete(models.Model):
    first_name = models.CharField(max_length=40,)
    last_name = models.CharField(max_length=40,)
    birth_date = models.DateField()
    threshold_hr = models.IntegerField()
    run_longest_distance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Training(models.Model):
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
        Athlete, on_delete=models.CASCADE, related_name='trainings')
    date = models.DateField()
    planned_duration = models.TimeField(blank=True, null=True)
    completed_duration = models.TimeField()
    hour_avg = models.TimeField()

    def __str__(self):
        return self.athlete

    def get_absolute_url(self):
        return reverse('athlete_info', kwargs={'pk': self.pk})
