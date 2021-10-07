from django.urls import path

from . import views

# add namespace for polls here
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    # int:question_id passes the question id (5 above) to views.detail
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#if somebody goes to an empty path in ur website open up views' index function
