from django.urls import include, path
from categories.views import router

urlpatterns = [
    path('api/', include(router.urls)),
]