from django.urls import path
from . import views #imports views from the same folder

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register')
]