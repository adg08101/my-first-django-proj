from django.contrib import admin

from .models import Question, Language, Choice, QuestionType, QuestionChoiceVote

admin.site.register(Question)
admin.site.register(Language)
admin.site.register(Choice)
admin.site.register(QuestionType)
admin.site.register(QuestionChoiceVote)
