from django.shortcuts import render,redirect 
from .models import Book
 
def home(request):
    book = Book.objects.all()
    return render(request,'home.html',{'book':book})
