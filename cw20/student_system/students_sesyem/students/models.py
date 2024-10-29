from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)

def __str__(self):
    return self.name