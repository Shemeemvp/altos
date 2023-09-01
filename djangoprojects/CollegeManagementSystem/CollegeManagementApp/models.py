from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField(null=True)
    course_fee = models.BigIntegerField(null=True)

class TeacherModel(models.Model):
    teacher_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    # teacher_info = models.ForeignKey(User)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(CourseModel, on_delete= models.CASCADE)
    address = models.TextField()
    image = models.ImageField(upload_to='image/')

class StudentModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(CourseModel, on_delete= models.CASCADE)
    address = models.TextField()
    image = models.ImageField(upload_to='image/')