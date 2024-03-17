# blog/urls.py
from django.urls import path
from . import views
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

app_name = 'selfsignlanguagetochatgpt'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('home', index),
]
