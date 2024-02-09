from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup_form(request):
    context = {}
    return render(request, 'signup.html', context)


def index(request):
    context ={}
    return render(request, 'index.html', context)
