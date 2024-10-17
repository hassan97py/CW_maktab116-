from django.urls import path
from .views import register,profile
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

