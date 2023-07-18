from django.db import models
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse("book_details", kwargs={"pk": self.pk})
