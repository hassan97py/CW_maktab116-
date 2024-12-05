# from rest_framework.permissions import IsAuthenticatedOrReadOnly 
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import generics

# class BookListCreateView(generics.ListCreateAPIView): 
#     queryset = Book.objects.all() 
#     serializer_class = BookSerializer 
#     permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework import viewsets
# from .models import Author, Book
# from .serializers import AuthorSerializer, BookSerializer
    
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
