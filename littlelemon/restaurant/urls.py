from . import views
from django.urls import path, include
from .views import MenuItemsListView

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("menu/", MenuItemsListView.as_view(), name="menu"),
]
