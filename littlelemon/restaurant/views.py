from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', main_data)


