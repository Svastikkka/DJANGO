from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello I am from fourth views.py'}
    return render(request, 'index/index.html', context=my_dict)
