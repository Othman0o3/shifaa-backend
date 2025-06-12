from rest_framework import generics
from .models import Doctor,hospital
from django.contrib.auth import login
from django.contrib.auth.models import User
from .serializers import DoctorSerializer,HospitalSerializer
from django.shortcuts import render
# Serializer (convert model to JSON)

#API View

def hospital_list_view(request):
    return render(request, 'hospital.html')
class HospitalListCreateAPI(generics.ListCreateAPIView):
    queryset = hospital.objects.all()
    serializer_class = HospitalSerializer
    filterset_fields = ['name']

class DoctorsByHospitalAPI(generics.ListAPIView):
    serializer_class = DoctorSerializer
    def get_queryset(self):
        hospital_id = self.kwargs['hospital_id']
        return Doctor.objects.filter(hospital_id=hospital_id)

class DoctorListAPI(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
