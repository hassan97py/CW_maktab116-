from django.urls import path, include
from .views import CategoryViewSet, SubcategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'categories/(?P<category_id>\d+)/subcategories', SubcategoryViewSet, basename='subcategory')

urlpatterns = [
    path('api/', include(router.urls)),
]
