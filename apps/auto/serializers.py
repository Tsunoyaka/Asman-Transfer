from rest_framework import serializers

from .models import Auto, Driver


class AutoSerializers(serializers.ModelSerializer): 
    class Meta:
        model = Auto
        fields = ('title', 'price', 'contract_price', 'description', 'capacity', 'photo')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('name', 'experience', 'photo')