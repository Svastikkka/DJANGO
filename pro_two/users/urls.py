from django.urls import path
from help import views
urlpatterns = [
    path(r'', views.index, name='help'),
]