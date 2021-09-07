from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

#Create your views here

def index(request):

    # - sign shows the reverse according to publication date to show recent ones first !
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # first 5 questions in the list

    output = ', '.join([q.question_text for q in latest_question_list])
    # list comprehensions in python

    context = {'latest_question_list': latest_question_list}
    # stuff for front end
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

