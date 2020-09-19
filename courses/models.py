from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class Class(models.Model):
    class_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, null=True, blank=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name


class Assignments(models.Model):
    message = models.TextField(null=True, blank=True)
    question = models.FileField(upload_to='assignment/questions/', blank=True)
    class_object = models.ForeignKey(
        Class, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_object.name


class Solutions(models.Model):
    assignment = models.ForeignKey(
        Assignments, null=True, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.FileField(upload_to='assignment/answer/', blank=True)

    def __str__(self):
        return self.student.user.username
