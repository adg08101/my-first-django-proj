from django.db import models
from django.utils import timezone
import datetime


class Language(models.Model):
    language_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.language_text


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    language = models.ForeignKey(Language, default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.question_text} --- {self.pub_date}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class QuestionType(models.Model):
    question = models.ManyToManyField(Question)
    type_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
