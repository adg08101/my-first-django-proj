from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"The question id is {self.id} with {self.question_text} text and added on {self.pub_date}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Note(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    note = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
