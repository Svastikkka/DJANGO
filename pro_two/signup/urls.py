from django.urls import path
from signup import views
urlpatterns = [
    path(r'', views.signup, name='signup'),
]