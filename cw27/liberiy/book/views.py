from rest_framework import viewsets
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated





# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]


