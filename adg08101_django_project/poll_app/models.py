from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime


class Language(models.Model):
    language_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.language_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.choice_text}"


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # type = models.ManyToManyField(QuestionType)
    choice = models.ManyToManyField(Choice)
    extra = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.question_text}"

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class QuestionType(models.Model):
    type_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    question_type = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.type_text}"


class QuestionChoiceVote(models.Model):
    question = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, default=None, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        votes = 'votes' if self.votes > 1 else 'vote'
        return f"{self.choice} response for {self.question} has {self.votes} {votes}"
