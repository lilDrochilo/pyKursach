from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data_main_page={
        'title': 'Добро пожаловать в нашу тату студию!',


    }
    return render(request, 'mainpage/index.html',data_main_page)

def about_master(request):
    data_about_master={
        'title': 'Привет!'
    }
    return render(request, 'mainpage/about_master.html')

def contacts(request):
    return render(request, 'mainpage/contacts.html')

