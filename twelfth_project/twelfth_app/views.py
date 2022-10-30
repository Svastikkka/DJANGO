from django.shortcuts import render

# Create your views here.


def twelfth_app(request):
    sample_dict = {'sample_context': 'Hello I am from home views', 'sample_number': '100'}
    return render(request, 'home/home.html', context=sample_dict)