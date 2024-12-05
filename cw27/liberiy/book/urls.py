# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet, MemberViewSet, LoanViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)
# router.register(r'members', MemberViewSet)
# router.register(r'loans', LoanViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
path('api/', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]