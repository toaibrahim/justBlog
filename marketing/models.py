import email
from sqlite3 import Timestamp
from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.EmailField()
    Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    email = models.EmailField(null=False)
    name = models.CharField(max_length=64,null=False)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email