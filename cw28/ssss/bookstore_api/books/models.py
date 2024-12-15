from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        # # Send email notification
        # send_mail(
        #     subject="Welcome to Bookstore API",
        #     message=f"Hello {phone_number}, your account has been successfully created!",
        #     from_email="tree123red@gmail.com",
        #     recipient_list=[extra_fields.get('email', 'tree123red@gmail.com')],
        #     fail_silently=False,
        # )
        # return user

    
class User(AbstractBaseUser):


    phone_number = PhoneNumberField(unique=True) 
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []
    objects = UserManager()


    def __str__(self):
        return str(self.phone_number)


class Author(models.Model):

    name = models.CharField(max_length=100) 
    biography = models.TextField(blank=True)

class Book(models.Model):


    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
