from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news_main_page'),
]