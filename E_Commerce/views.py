from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password , check_password


def signup_form(request):
    context = {}
    return render(request, 'signup.html', context)

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_in_process = request.POST.get('password')
        password = make_password(password_in_process)
        user = User(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('index')
    return redirect('index')

def login_form(request):
    context = {}
    return render(request, 'login.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
              return render(request, 'login.html', {"error": "Email or password is invalid"})
    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('login_form')


def index(request):
    context ={}
    return render(request, 'index.html', context)
