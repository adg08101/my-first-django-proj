from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Main App index view.")
# Create your views here.
