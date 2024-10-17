from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from accounts.models import CustomUser 

def profile(request):
    
    username=CustomUser.objects.all()
    return render(request, 'accounts/profile.html', context={"user.username": request.user.username})
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})