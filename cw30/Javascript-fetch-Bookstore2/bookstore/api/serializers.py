# from rest_framework import serializers
# from .models import Book, Author

# class AuthorSerializer(serializers.ModelSerializer):
#     books = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Author
#         fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()

#     class Meta:
#         model = Book
#         fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

#     class Meta:
#         model = Book
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Author, Book

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id', 'name', 'biography']

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())  # استفاده از شناسه نویسنده

#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'description', 'published_date', 'author']
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())  # برای افزودن کتاب
    author_name = serializers.CharField(source='author.name', read_only=True)  # برای نمایش نام نویسنده

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'published_date', 'author', 'author_name']
