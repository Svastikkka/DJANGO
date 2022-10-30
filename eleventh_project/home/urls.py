from django.urls import path
from home import views
urlpatterns = [
    path(r'', views.home, name='home'),
]