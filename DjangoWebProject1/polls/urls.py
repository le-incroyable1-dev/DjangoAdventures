from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#if somebody goes to an empty path in ur website open up views' index function
