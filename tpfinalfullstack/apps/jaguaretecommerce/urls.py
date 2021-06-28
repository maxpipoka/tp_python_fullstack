from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'), #views es el nombre del modulo phython, .blog es el nombre de la funcino, y el name es como se va a redirigir el path
]