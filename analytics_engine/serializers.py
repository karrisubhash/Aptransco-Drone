from rest_framework import serializers

from .models import (
    Tower,
    Inspection,
    Defect,
    Prediction
)


class TowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tower
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'