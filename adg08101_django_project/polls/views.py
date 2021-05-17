from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db.models import F
from django.template import loader
from django.views import defaults, generic
import requests, datetime, socket
from django.views.decorators.csrf import csrf_exempt


class LatestQuestionsGenericView(generic.ListView):
    message = None


class LatestQuestionsView(LatestQuestionsGenericView):
    message = 'HolaMundo!!!'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
                 Return the last five published questions (not including those set to be
                 published in the future).
                 """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    def head(self, *args, **kwargs):
        """
            Return the last five published questions (not including those set to be
            published in the future).
            """
        lastest = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        response = HttpResponse(
            headers={
                'latest': lastest,
                'message': self.message,
            })
        return response


class QuestionDetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def head(self, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs.get('pk'))
        response = HttpResponse(
            headers={'question': question},
        )
        return response


class ResultsView(generic.DetailView):
    model = Question

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    template_name = 'poll/results.html'


def getContext(message=None):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
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
    if request.method == 'HEAD':
        lastest = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        response = HttpResponse(
            headers={
                'latest': lastest,
            })
        return response

    try:
        template = loader.get_template('polls/index.html')
        context = getContext()
        return HttpResponse(template.render(context, request))
    finally:
        if 'message' in request.session:
            del request.session['message']


def new(request):
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


def details(request, pk):
    question = Question.objects.get(id=pk)
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

    # q.type.add(QuestionType.objects.get(pk=request.POST['type']))

    for i in l:
        q.choice.add(Choice.objects.get(pk=i))

    q.save()

    request.session['message'] = 'Question added'
    template = loader.get_template('polls/index.html')
    return HttpResponseRedirect(reverse('polls:index'))


def results(request, pk, year, bla, theme):
    if year < 2000:
        century = '20th'
    else:
        century = '21th'

    response = f"You're looking at the results of question {pk} for year {year} on {century}" \
               f"century says {bla}. for {theme} theme"
    return HttpResponse(response)


def questions_results(request):
    question_choices_votes = QuestionChoiceVote.objects.all().order_by('question')
    template = loader.get_template('polls/results.html')
    context = {
        'results': question_choices_votes,
    }
    return HttpResponse(template.render(context, request))


def vote(request, pk):
    try:
        template = loader.get_template('polls/vote.html')
        q = Question.objects.get(pk=pk)
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


def delete(request, pk):
    url = 'http://127.0.0.1:8000/polls/' + str(pk) + '/do_delete'
    response = requests.delete(
        url=url,
    )

    request.session['message'] = 'Question deleted'
    template = loader.get_template('polls/index.html')
    return HttpResponseRedirect(reverse('polls:index'))


@csrf_exempt
def do_delete(request, pk):
    if request.method == 'DELETE':
        try:
            q = get_object_or_404(Question, pk=pk)
            q.delete()
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
