from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book:list")