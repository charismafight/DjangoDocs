from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ','.join([x.question_text for x in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("you're looking at %s" % question_id)


def results(request, question_id):
    return HttpResponse("you're looking at results of %s." % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on %s." % question_id)
