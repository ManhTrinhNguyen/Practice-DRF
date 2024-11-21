from django.db import models

# Create your models here.
class BooksModel(models.Model):
  title = models.CharField(max_length=250)
  author = models.CharField(max_length=250)
  genre = models.CharField(max_length=100)
  is_available = models.BooleanField(default=True)

  def __str__(self):
    return self.title 

class UsersModel(models.Model):
  name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.name 

class TransactionsModel(models.Model):
  user = models.ForeignKey(UsersModel, on_delete=models.CASCADE ,related_name='user')
  book = models.ForeignKey(BooksModel, on_delete=models.CASCADE ,related_name='book')
  borrow_date = models.DateTimeField(auto_now_add=True)
  return_date = models.DurationField(blank=True, null=True)

  def __str__(self):
    return f'{self.book.title} borrowed by {self.user.name}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    # Update book availability 
    if not self.return_date:
      self.book.is_available = False
    else:
      self.book.is_available = True 

    self.book.save()

  
