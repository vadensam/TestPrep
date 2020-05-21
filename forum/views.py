from django.shortcuts import render
from login.models import User
from .models import Book, Review

def home(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user' : user,
        'all_books' : Book.objects.all(),
    }
    return render(request, 'user.html', context)

def add_book(request):
    return render(request, 'add_book.html')