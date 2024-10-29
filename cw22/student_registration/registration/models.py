from django.db import models
from datetime import datetime
from django import utils
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)

    def clean(self):
        if self.age <= 10:
            raise Exception('Age must be greater than 10.')

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registration')
    registration_time = models.DateTimeField(auto_now_add=True)
    session_data = models.TextField(default='')