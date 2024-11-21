from django.contrib import admin
from .models import TransactionsModel, UsersModel, BooksModel

# Register your models here.
admin.site.register(TransactionsModel)
admin.site.register(UsersModel)
admin.site.register(BooksModel)
