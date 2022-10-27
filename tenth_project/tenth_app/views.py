from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index/index.html')


def other(request):
    return render(request, 'other/other.html')


def relative(request):
    return render(request, 'relative_url_template/relative_url_template.html')