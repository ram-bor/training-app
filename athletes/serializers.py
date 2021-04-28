from rest_framework import serializers
from .models import Athlete, Training


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    training = serializers.HyperlinkedRelatedField(
        view_name='athlete_info',
        many=True,
    )

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'birth_date',
                  'threshold_hr', 'run_longest_distance', 'training')
