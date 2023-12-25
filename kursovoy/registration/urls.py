from django.urls import path
from . import views

urlpatterns = [

    path('', views.registration_home, name='registration_home'),
    path('registration_home', views.regist, name='registration_home'),
]