from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all() #order_by('-created_at')
    context = {
        'news': news,
        'title': 'News list:',
    }
    return render(request, 'news/index.html', context)

def test(request):
    return HttpResponse('<h1>Test REQUEST</1>')