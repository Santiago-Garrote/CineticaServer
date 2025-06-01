from rest_framework import serializers
from apps.Images.models import ObservationImage


class CreateObservationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationImage
        fields = '__all__'
