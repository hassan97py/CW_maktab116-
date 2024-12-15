from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Category, Subcategory
from .serializers import CategorySerializer, SubcategorySerializer
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer

    class SubcategoryViewSet(viewsets.ModelViewSet):
        serializer_class = SubcategorySerializer

        def get_queryset(self):
            category_id = self.kwargs.get('category_id')
            if category_id is not None:
                return Subcategory.objects.filter(category_id=category_id)
            return Subcategory.objects.none()  

    def create(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        request.data['category'] = category_id
        return super().create(request, *args, **kwargs)



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'categories/(?P<category_id>\d+)/subcategories', SubcategoryViewSet)