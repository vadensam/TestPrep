from django.urls import path
from . import views

urlpatterns = [
    path('books', views.home),
    path('add_book', views.add_book),
]