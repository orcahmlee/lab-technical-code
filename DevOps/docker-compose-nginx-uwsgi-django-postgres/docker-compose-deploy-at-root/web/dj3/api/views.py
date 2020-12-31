from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("I am Django 3.1 !!!")
