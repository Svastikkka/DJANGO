from django.urls import path
from users import views
urlpatterns = [
    path(r'', views.index, name='users'),
]