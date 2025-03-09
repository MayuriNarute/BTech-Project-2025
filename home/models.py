from django.db import models
from django.contrib.auth.models import User


class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # Store hashed passwords
    role = models.CharField(max_length=20, choices=[('doctor', 'Doctor'), ('lab_assistant', 'Lab Assistant')])

    # Additional Fields
    license = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    hospital = models.CharField(max_length=200, blank=True, null=True)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    lab_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
