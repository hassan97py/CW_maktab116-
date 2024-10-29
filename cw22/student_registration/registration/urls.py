from django.urls import path
from .views import register_student, success, student_list

urlpatterns = [
path('register/', register_student, name='register'),
path('success/', success, name='success'),
path('students/', student_list, name='student_list'), # New URL for student list
]