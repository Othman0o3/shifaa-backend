import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from doctors.models import Doctor, Patient  # Import your profile models
from django.http import JsonResponse
from django.shortcuts import render

def doctor_dashboard(request):
    return render(request, 'dashboard/doctor.html')

def patient_dashboard(request):
    return render(request, 'dashboard/patient.html')

def lab_dashboard(request):
    return render(request, 'dashboard/lab.html')
@csrf_exempt
def signup_view(request):    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            age = data.get('age')
            gender = data.get('gender')
            email = data.get('email')
            password = data.get('password')
            user_type = data.get('user_type')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            user = User.objects.create_user(username=username, password=password)

            if user_type == 'doctor':
                Doctor.objects.create(user=user)
            elif user_type == 'patient':
                Patient.objects.create(user=user)

            login(request, user)
            return JsonResponse({'message': 'Signup successful', 'user_type': user_type}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)