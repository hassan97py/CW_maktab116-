from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Check if user is superuser
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def student_list(request):
    students = Student.objects.all() # Retrieve all registered students
    return render(request, 'student_registration/student_list.html', {'students': students})

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            response = redirect('success')
            response.set_cookie('student_name', student.name)

            messages.success(request, 'Registration successful!')
            return response
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_registration/register.html', {'form': form})

def success(request):
    student_name = request.COOKIES.get('student_name', 'Guest')
    return render(request, 'student_registration/success.html', {'student_name': student_name})