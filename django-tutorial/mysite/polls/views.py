from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Django!')

def detail(request, question_id):
    return HttpResponse(f'question {question_id} details')

def results(request, question_id):
    return HttpResponse(f'results of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'vote on question {question_id}')
