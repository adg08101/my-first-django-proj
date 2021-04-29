from django.db import models
from django.utils import timezone
import datetime


class Language(models.Model):
    language_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.language_text


class QuestionType(models.Model):
    type_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.type_text}"


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.choice_text}"


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    type = models.ManyToManyField(QuestionType)
    choice = models.ManyToManyField(Choice)
    extra = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.question_text} " + datetime.datetime.strftime(self.pub_date, '%b %d, %Y')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class QuestionChoiceVote(models.Model):
    question = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, default=None, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        votes = 'votes' if self.votes > 1 else 'vote'
        return f"{self.choice} response for {self.question} has {self.votes} {votes}"
