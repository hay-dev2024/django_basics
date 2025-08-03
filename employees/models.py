from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True) # blank=True -> optional
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add -> use it when the data is being saved for the first time
    updated_at = models.DateTimeField(auto_now=True)

