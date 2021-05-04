from rest_framework import serializers
from .models import Athlete, Training


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    training = serializers.HyperlinkedRelatedField(
        view_name='athlete_info',
        many=True,
        read_only=True
    )
    athlete_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'birth_date',
                  'threshold_hr', 'run_longest_distance', 'training')
