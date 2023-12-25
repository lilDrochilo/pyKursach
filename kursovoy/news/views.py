from django.shortcuts import render
from .models import News
def news_main(request):
    news = News.objects.order_by('-date')[:4]
    return render(request, 'news/news_main_page.html', {'news':news})
