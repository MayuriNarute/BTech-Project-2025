from django.db import models

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)