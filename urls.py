
from django.contrib import admin
from django.urls import path
from djangoProject_test import views

urlpatterns = [
    path('', views.bookList),
    path('book/<int:id>/', views.GetBook, name='book_url')
]
