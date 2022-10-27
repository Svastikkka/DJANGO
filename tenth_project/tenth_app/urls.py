from django.urls import path
from tenth_app import views

# TEMPLATE TAGGING
app_name = 'tenth_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
