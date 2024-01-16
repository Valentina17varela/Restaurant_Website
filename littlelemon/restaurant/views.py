from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import RecomendationForm
from django.contrib import messages
from .models import Recomendation, MenuItems
from django.views.generic import ListView


def home(request):
    recommendations = Recomendation.objects.order_by("-created_at")[:5]
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

    return render(request, "home.html", {"recommendations": recommendations})


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def book(request):
    return HttpResponse("Hello world!")


class MenuItemsListView(ListView):
    model = MenuItems
    template_name = "menu.html"
    context_object_name = "menu_items"

    def get_queryset(self):
        return MenuItems.objects.all()
