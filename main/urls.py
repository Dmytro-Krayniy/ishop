from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]