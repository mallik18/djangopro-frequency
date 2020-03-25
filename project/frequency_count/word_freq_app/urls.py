from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='Word_Freq_Home'),
    path('about/', views.about , name='Word_Freq_About')
]
