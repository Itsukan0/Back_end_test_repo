# models.py de Django
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    pages = models.IntegerField()
    language = models.CharField(max_length=2)
    isborrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
