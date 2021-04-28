from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request, desde='main'):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    questions = Question.objects.all()

    context = {
        'latest_question_list': latest_question_list,
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))


# Create your views here.
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    template = loader.get_template('polls/detail.html')
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id, year, bla, theme):
    if year < 2000:
        century = '20th'
    else:
        century = '21th'

    response = f"You're looking at the results of question {question_id} for year {year} on {century}" \
               f"century says {bla}. for {theme} theme"
    return HttpResponse(response)


def vote(request, question_id=1, month_id=1):
    return HttpResponse(f"You're voting on question {question_id} for month {month_id}")

def delete(request, question_id):
    q = Question.objects.get(pk = question_id)
    q.delete()
    template = loader.get_template('polls/delete.html')
    return HttpResponse(template.render(request=request))
