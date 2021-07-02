from django.db import models
from django.contrib.auth.admin import User


# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=20, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description
