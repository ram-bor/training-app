from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Athlete, Training


class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'birth_date',
                  'threshold_hr', 'run_longest_distance',)


class TrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('sport_type', 'athlete', 'date',
                  'planned_duration', 'duration', 'hour_avg',)


class DateForm(forms.ModelForm):
    date = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )
