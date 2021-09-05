from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#if somebody goes to an empty path in ur website open up views' index function
