from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello,world.You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("you're looking at %s" % question_id)


def results(request, question_id):
    return HttpResponse("you're looking at results of %s." % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on %s." % question_id)