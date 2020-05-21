from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        email = request.POST['email'],
        password = pw_hash,
    )
    request.session['id'] = user.id
    return redirect('forum/books')

def login(request):
    user_db = User.objects.filter(email=request.POST['email'])
    if user_db:
        log_user = user_db[0]

        if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
            request.session['id'] = log_user.id
            return redirect('/books')

    messages.error(request, 'Incorrect email or password.')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')