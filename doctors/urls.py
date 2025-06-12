from django.urls import path
from .views import DoctorListAPI,DoctorsByHospitalAPI,HospitalListCreateAPI

urlpatterns = [
    path('doctors/',DoctorListAPI.as_view(),name='DoctorList'),
    path('hospitals/', HospitalListCreateAPI.as_view(),name='hospital-list'),
    # path('hospitals/<int:hospital_id>/doctors/', DoctorsByHospitalAPI.as_view()),

]