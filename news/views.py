from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(res):
    return HttpResponse("Hello, world. You're at the news index.")


def about(request):
    return HttpResponse("This is the about page")


def gallery(request,page):
    return HttpResponse(f"This is the gallery page {page}")
