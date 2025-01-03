# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class UserModel(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.phone_number} - {self.date_of_birth}"
