from django.views import generic as views
from django.shortcuts import render



class IndexView(views.ListView):
    template_name = 'index.html'

