from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')

def about_master(request):
    return render(request, 'mainpage/about_master.html')

def contacts(request):
    return render(request, 'mainpage/contacts.html')

