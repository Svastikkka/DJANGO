from django.urls import path
from twelfth_app import views
urlpatterns = [
    path(r'', views.twelfth_app, name='twelfth_app'),
]