from django.db import models

# Create your models here.
class Book(models.Model):
    bookid = models.IntegerField()
    bookname= models.CharField(("Bname"),max_length=20)
    bookgenere = models.CharField(("Bgenere"),max_length=20)
    bcost = models.FloatField()