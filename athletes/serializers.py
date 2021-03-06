from rest_framework import serializers
from .models import Athlete, Training


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    trainings = serializers.HyperlinkedRelatedField(
        view_name='athlete_info',
        many=True,
        read_only=True
    )
    athlete_url = serializers.ModelSerializer.serializer_url_field(
        view_name='athlete_info'
    )

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'birth_date',
                  'threshold_hr', 'run_longest_distance', 'trainings', 'athlete_url')


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    training = serializers.PrimaryKeyRelatedField(
        queryset=Athlete.objects.all())

    class Meta:
        model = Training
        fields = ('id', 'athlete', 'sport_type', 'date',
                  'planned_duration', 'completed_duration', 'hour_avg')
