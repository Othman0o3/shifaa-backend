from django.urls import path
from .views import signup_view, doctor_dashboard, patient_dashboard, lab_dashboard

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),
    path('dashboard/lab/', lab_dashboard, name='lab_dashboard'),
]