from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.example, name='home'),
    path("about", views.about, name='aboutpage'),
    path("service", views.service, name='servicepage'),
    path("contact", views.contact, name='contactpage'),
]