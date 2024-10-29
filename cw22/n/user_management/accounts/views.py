from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from accounts.models import CustomUser 

def profile(request):
    # Ensure the user is authenticated before accessing the profile
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html', {
            'username': request.user.username,
            'email': request.user.email,
            'phone_number': request.user.phone_number,
            'date_of_birth': request.user.date_of_birth
        })
    else:
        return redirect('login')  # Redirect to login if not authenticated

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
