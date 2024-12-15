from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet
from django.urls import path, include

# Root router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

# Nested router for subcategories
categories_router = NestedDefaultRouter(router, r'categories', lookup='category')
categories_router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')

urlpatterns = [
    path('', include(router.urls)),  # Includes category routes
    path('', include(categories_router.urls)),  # Includes nested subcategory routes
]
