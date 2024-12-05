from rest_framework import serializers 
from .models import Author, Book 
 
class AuthorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Author 
        fields = ['id', 'name', 'biography', 'books'] 
 
class BookSerializer(serializers.ModelSerializer): 
    author = serializers.HyperlinkedRelatedField( 
        view_name='author-detail', 
        read_only=True 
    ) 
 
    class Meta: 
        model = Book 
        fields = ['id', 'title', 'description', 'published_date', 'author']