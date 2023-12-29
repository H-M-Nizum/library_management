from django.db import models
from django.contrib.auth.models import User
from library.models import BookModel

# Create your models here.
class UserAccountModel(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_length=12, max_digits=1000000000000, decimal_places=2)
    
    def __str__(self):
        return str(self.account_no)
    
class BorrowedBook(models.Model):
    user = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
# model for comment

class Comment(models.Model):
    # related ar value diye ai field ta access kora jabe
    book = models.ForeignKey(BookModel, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    # unique = true means ak e email diye multiple comment korte parbe na.
    email = models.EmailField()
    body = models.TextField()
    # auto coment ar date time show korbe
    created_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"comment by {self.name}"