from django.shortcuts import render
from users.models import users


# Create your views here.

def index(request):
    users_list = users.objects.order_by('first_name')
    user_dict = {'users_records': users_list}
    return render(request, 'users/users.html', context=user_dict)
