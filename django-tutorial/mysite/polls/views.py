from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
# from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse(f'question {question_id} details')

def results(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    # return HttpResponse(f'results of question {question_id}')
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    return HttpResponse(f'vote on question {question_id}')
