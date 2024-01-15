from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def book(request):
    return HttpResponse("Hello world!")


def menu(request):
    return HttpResponse("Hello world!")


def menu_item(request):
    return HttpResponse("Hello world!")
