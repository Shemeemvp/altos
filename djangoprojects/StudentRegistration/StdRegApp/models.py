from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(max_length=250)
    course = models.CharField(max_length=50)
    address = models.TextField()