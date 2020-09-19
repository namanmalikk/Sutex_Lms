from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=100, null=True)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
