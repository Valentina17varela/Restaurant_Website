from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.menu_item, name='menu_item'),
]
