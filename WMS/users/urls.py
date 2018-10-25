from django.urls import path, include
from . import views #imports views from the same folder

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('', include('django.contrib.auth.urls')), #Gives inbuilt urls for user management system
]