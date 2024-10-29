
from django.contrib import admin
from django.urls import path
from calculator_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/<str:a>/<str:b>/', views.add, name='add'),
    path('subtract/<str:a>/<str:b>/', views.subtract, name='subtract'),
    path('multiply/<float:a>/<float:b>/', views.multiply, name='multiply'),
    path('divide/<float:a>/<float:b>/', views.divide, name='divide'),
]
