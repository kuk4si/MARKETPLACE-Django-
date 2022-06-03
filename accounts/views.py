from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('/')



def login(request):
    pass


def register(request):
    pass