from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    data = {
        'title': 'Головна',
        'content': 'Main page of ishop',
        'categories': Categories.objects.all()
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    data = {
        'title': 'О нас',
        'content': 'About page of ishop',
    }
    return render(request, 'main/about.html', context=data)
