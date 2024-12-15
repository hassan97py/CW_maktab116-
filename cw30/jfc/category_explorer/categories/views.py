from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Category, Subcategory
from .serializers import CategorySerializer, SubcategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class SubcategoryViewSet(viewsets.ModelViewSet):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def perform_create(self, serializer):
        # اگر می‌خواهید کاربر را به عنوان دسته تعیین کنید
        serializer.save(category=self.get_category())

    def get_category(self):
        category_id = self.kwargs['category_id']
        return Category.objects.get(id=category_id)
    
    
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'categories/(?P<category_id>\d+)/subcategories', SubcategoryViewSet)
