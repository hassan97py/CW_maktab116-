from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

#     class Meta:
#         model = Book
#         fields = '__all__'

