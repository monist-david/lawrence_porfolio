# -*- coding: utf-8 -*-

from django.urls import path
from .views import HomeView


app_name = 'porfolio'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]