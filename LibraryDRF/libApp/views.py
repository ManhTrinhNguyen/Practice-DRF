from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from .models import BooksModel, TransactionsModel
from .serializers import BookSerializer, TransactionSerializer

# Create your views here.
@api_view()
def books(request):
  books = BooksModel.objects.all()
  serializer_books = BookSerializer(books, many=True)
  return Response(serializer_books.data)

@api_view()
def book(request, pk):
  book = get_object_or_404(BooksModel, pk=pk)
  serializer_book = BookSerializer(book)
  return Response(serializer_book.data)

@api_view()
def transactions(request):
  transactions = TransactionsModel.objects.all()
  serializer_transactions = TransactionSerializer(transactions, many=True)
  return Response(serializer_transactions.data)