from django.shortcuts import render

# Create your views here.
from djangoProject_test.models import Book
from datetime import date

def bookList(request):
    return render(request, 'books.html', {'data': {
        'current_date': date.today(),
        'books': Book.objects.all()
    }})


def GetBook(request, id):
    return render(request, 'book.html', {'data': {
        'current_date': date.today(),
        'book': Book.objects.filter(id=id)[0]
    }})
