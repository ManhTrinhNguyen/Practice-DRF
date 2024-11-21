from rest_framework import serializers 
from .models import TransactionsModel, UsersModel, BooksModel 

# class BookSerializer(serializers.Serializer):
#   id = serializers.IntegerField()
#   title = serializers.CharField(max_length=200)
#   author = serializers.CharField(max_length=200)
#   is_available = serializers.BooleanField(default=True)

class BookSerializer(serializers.ModelSerializer):
  is_available = serializers.SerializerMethodField(method_name='set_available')
  class Meta:
    model = BooksModel
    fields = ['title', 'author', 'genre', 'is_available']

  # Set method if book is borrowed or not 
  def set_available(self, book: BooksModel):
    # Check if there are any transactions (borrowed but not returned) for the book
    active_transactions = TransactionsModel.objects.filter(book=book, return_date__isnull=True).exists()
    return not active_transactions
    

class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=250)
  email = serializers.EmailField()
  is_active = serializers.BooleanField(default=True)


class TransactionSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField()
  book = serializers.StringRelatedField()
  class Meta:
    model = TransactionsModel
    fields = ['borrow_date', 'return_date', 'user', 'book']


  