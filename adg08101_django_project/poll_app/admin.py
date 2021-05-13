from django.contrib import admin

from .models import Question, Language, Choice, QuestionType, QuestionChoiceVote

class QuestionTypeInline(admin.TabularInline):
    model = QuestionType
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Question', {
            'fields': [
                'question_text'
            ]
        }),
        ('Languague', {
            'fields': [
                'language'
            ], 'classes': ['collapse']
        }),
        ('Dates', {
            'fields': [
                'pub_date'
            ], 'classes': ['collapse']
        })
    ]
    inlines = [QuestionTypeInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Language)
admin.site.register(Choice)
admin.site.register(QuestionType)
admin.site.register(QuestionChoiceVote)
