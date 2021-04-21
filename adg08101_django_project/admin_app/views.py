from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the index view on Admin App")
# Create your views here.