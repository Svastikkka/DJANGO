from django.shortcuts import render
from users.models import users


# Create your views here.

def index(request):
    webpages_list = users.objects.order_by('name')
    date_dict = {'access_records': webpages_list}

    return render(request, 'users/users.html', context=date_dict)
