from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserAccountModel)
admin.site.register(models.BorrowedBook)
admin.site.register(models.Comment)