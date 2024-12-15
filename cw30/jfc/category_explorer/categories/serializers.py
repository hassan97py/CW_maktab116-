from rest_framework import serializers
from .models import Category, Subcategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# class SubcategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subcategory
#         fields = ['id', 'category', 'name']
        
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'category', 'name']

    def create(self, validated_data):
        category = validated_data.pop('category')
        subcategory = Subcategory.objects.create(category=category, **validated_data)
        return subcategory
