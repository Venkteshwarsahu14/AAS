from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import vehicle



class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'