from django.shortcuts import render

def registration_home(request):
    return render(request, 'registration/registration_home.html')

def regist(request):
    return render(request, 'registration/registration_home.html')


