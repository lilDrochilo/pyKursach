from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_master', views.about_master, name='about_master'),
    path('contacts', views.contacts, name='contacts')

]