from django.shortcuts import render

# Create your views here.


def home(request):
    sample_dict = {'sample_context': 'Hello I am from home views'}
    return render(request, 'home/home.html', context=sample_dict)
