from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import RecomendationForm
from django.contrib import messages
from .models import Recomendation, MenuItems, Book
from django.views.generic import ListView


def home(request):
    recommendations = Recomendation.objects.order_by("-created_at")[:5]
    menu_items = MenuItems.objects.all()[:3]
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

    return render(
        request,
        "home.html",
        {"recommendations": recommendations, "menu_items": menu_items},
    )


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())


def book(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        identification_number = request.POST.get("identification_number")
        phone_number = request.POST.get("phone_number")
        guests = request.POST.get("guests")
        reservation_date = request.POST.get("reservation_date")
        reservation_time = request.POST.get("reservation_time")

        booking = Book(
            first_name=first_name,
            last_name=last_name,
            identification_number=identification_number,
            phone_number=phone_number,
            guests=guests,
            reservation_date=reservation_date,
            reservation_time=reservation_time,
        )
        booking.save()
        messages.success(request, "Thanks for your booking!")

        return render(request, "book.html", {"booking": booking})

    return render(request, "book.html")


class MenuItemsListView(ListView):
    model = MenuItems
    template_name = "menu.html"
    context_object_name = "menu_items"

    def get_queryset(self):
        return MenuItems.objects.all()
