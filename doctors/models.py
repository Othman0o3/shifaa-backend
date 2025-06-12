from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # Optional, usually you use user.password

    def __str__(self):
        return self.name
class hospital(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    location_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Google Maps Link",
        help_text="e.g.: https://goo.gl/maps/..."
    )
    phone = models.CharField(max_length=12)
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    hospital = models.ForeignKey(
        'doctors.hospital', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="hospital")
    available_from = models.TimeField()
    available_to = models.TimeField()


def __str__(self):
    return f"{self.name} ({self.speciality})"
def __str__(self):
    return self.name
