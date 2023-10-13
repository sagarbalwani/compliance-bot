# bot/urls.py
from django.urls import path
from .views import qeuryChatBot

urlpatterns = [
    path("", qeuryChatBot, name="qeuryChatBot"),
]