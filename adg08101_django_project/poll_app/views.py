from django.shortcuts import render
from django.http import HttpResponse


def index(request, desde='main'):
    return HttpResponse(f"Hello, world. You're at the polls index. Desde {desde}")


# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id, year, bla, theme):
    if year < 2000:
        century = '20th'
    else:
        century = '21th'

    response = f"You're looking at the results of question {question_id} for year {year} on {century}" \
               f"century says {bla}. for {theme} theme"
    return HttpResponse(response)


def vote(request, question_id = 1, month_id = 1):
    return HttpResponse(f"You're voting on question {question_id} for month {month_id}")
