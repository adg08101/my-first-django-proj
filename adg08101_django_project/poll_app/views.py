from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db.models import F
from django.template import loader
import requests, datetime

def getContext(message=None):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    questions = Question.objects.all()
    questions_with_choices = []

    for q in questions:
        if q.choice.count() > 0:
            questions_with_choices.append(q)

    context = {
        'latest_question_list': latest_question_list,
        'questions': questions,
        'questions_with_choices': questions_with_choices,
        'message': message,
    }
    return context


def index(request):
    try:
        template = loader.get_template('polls/index.html')
        context = getContext()
        return HttpResponse(template.render(context, request))
    finally:
        if 'message' in request.session:
            del request.session['message']


# Create your views here.
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    template = loader.get_template('polls/detail.html')
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))


def new(request):
    # question = Question.objects.get(id=question_id)
    languages = Language.objects.all()
    types = QuestionType.objects.all()
    choices = Choice.objects.all()
    template = loader.get_template('polls/new.html')
    context = {
        'languages': languages,
        'types': types,
        'choices': choices,
    }
    return HttpResponse(template.render(context, request))


def details(request, question_id):
    question = Question.objects.get(id=question_id)
    template = loader.get_template('polls/details.html')
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    l = request.POST.getlist('choices[]')

    q = Question(question_text=request.POST['text'],
                    pub_date=datetime.datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M'),
                    language=Language.objects.get(pk=request.POST['lang']),
                    extra=None)

    q.save()

    q.type.add(QuestionType.objects.get(pk=request.POST['type']))

    for i in l:
        q.choice.add(Choice.objects.get(pk = i))

    q.save()

    request.session['message'] = 'Question added'
    template = loader.get_template('polls/index.html')
    return HttpResponseRedirect(reverse('polls:index'))


def results(request, question_id, year, bla, theme):
    if year < 2000:
        century = '20th'
    else:
        century = '21th'

    response = f"You're looking at the results of question {question_id} for year {year} on {century}" \
               f"century says {bla}. for {theme} theme"
    return HttpResponse(response)


def questions_results(request):
    question_choices_votes = QuestionChoiceVote.objects.all().order_by('question')
    template = loader.get_template('polls/results.html')
    context = {
        'results': question_choices_votes,
    }
    return HttpResponse(template.render(context, request))


def vote(request, question_id):
    try:
        template = loader.get_template('polls/vote.html')
        q = Question.objects.get(pk=question_id)
        c = Choice.objects.get(pk=request.POST['choice'])
        rel = QuestionChoiceVote.objects.filter(question=q, choice=c)
        context = {
            'question': q,
            'choice': c,
        }
        if rel.count() > 0:
            QuestionChoiceVote.objects.filter(question=q, choice=c).update(votes=F('votes') + 1)
        else:
            QuestionChoiceVote.objects.create(question=q, choice=c, votes=1)
    except:
        raise Http404("Object does not exist")

    return HttpResponse(template.render(request=request, context=context))


def delete(request, question_id):
    try:
        q = get_object_or_404(Question, pk=question_id)
        q.delete()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    finally:
        request.session['message'] = 'Question deleted'
        template = loader.get_template('polls/index.html')
        return HttpResponseRedirect(reverse('polls:index'))
