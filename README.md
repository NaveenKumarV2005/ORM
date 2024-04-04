# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

'''
admin.py

from django.contrib import admin
from .models import Book
admin.site.register(Book)

model.py

from django.db import models
class Book(models.Model):
    bookid = models.IntegerField()
    bookname= models.CharField(("Bname"),max_length=20)
    bookgenere = models.CharField(("Bgenere"),max_length=20)
    bcost = models.FloatField()
'''

## OUTPUT

![OUTPUT](./image.png)

![OUTPUT](./webpage%20out.png)

![OUTPUT](./web%20map.png)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
