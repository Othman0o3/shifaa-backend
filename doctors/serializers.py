from rest_framework import serializers
from .models import Doctor,hospital
class HospitalSerializer(serializers.ModelSerializer):
    location_link = serializers.URLField(required=False, allow_null=True)
    class Meta:
        model = hospital
        fields = ['name','location_link','address']
class DoctorSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
