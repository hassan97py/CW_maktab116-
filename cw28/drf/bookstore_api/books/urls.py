from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import AuthorListCreateView, BookListCreateView, AuthorViewSet, BookViewSet
 
 
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet) 
urlpatterns = [ 
    path('api/', include(router.urls)),
    path('authors/', AuthorListCreateView.as_view(), name='author-list'), 
    # path('authors/<int:pk>/', AuthorViewSet.as_view(), name='author-detail'), 
    path('books/', BookListCreateView.as_view(), name='book-list'), 
    # path('books/<int:pk>/', BookViewSet.as_view(), name='book-detail'), 
]