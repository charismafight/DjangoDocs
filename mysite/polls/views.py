from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ','.join([x.question_text for x in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': q})


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    # get selected choice
    # docs: selected_choice = q.choice_set.get(pk=request.POST['choice'])
    # infact we can use shortcut
    try:
        selected_choice = get_object_or_404(Choice, id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirect
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id, )))
