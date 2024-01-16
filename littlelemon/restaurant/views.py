from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import RecomendationForm
from django.contrib import messages


def home(request):
    if request.method == "POST":
        form = RecomendationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect("home")
        else:
            messages.error(request, "Something went wrong, try again!")
    else:
        form = RecomendationForm()

    return render(request, "home.html", {"form": form})


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def book(request):
    return HttpResponse("Hello world!")


def menu(request):
    return HttpResponse("Hello world!")


def menu_item(request):
    return HttpResponse("Hello world!")
