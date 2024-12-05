from rest_framework import serializers
from .models import Book, Member, Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    member_name = serializers.ReadOnlyField(source='member.name')

    class Meta:
        model = Loan
        fields = '__all__'

    def validate(self, data):
        if data['return_date'] and data['return_date'] < data['loan_date']:
            raise serializers.ValidationError("Return date cannot be before loan date.")
        return data

    def create(self, validated_data):
        book = validated_data['book']
        if book.stock <= 0:
            raise serializers.ValidationError("Book stock is zero.")
        book.stock -= 1
        book.save()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'return_date' in validated_data and validated_data['return_date']:
            instance.book.stock += 1
            instance.book.save()
        return super().update(instance, validated_data)
