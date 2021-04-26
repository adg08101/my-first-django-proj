from django.contrib import admin

from .models import Entry, Author, Blog

admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Blog)