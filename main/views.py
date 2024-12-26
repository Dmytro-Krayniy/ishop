from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'content': 'Main page of ishop',
        'list': ['first', 'second'],
        'dict': {'name': 'Mit', 'money': '1 million $'},
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    return HttpResponse('<h2 style="color:blue">About us page</h2>')