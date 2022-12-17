from django.views import generic as views
from django.shortcuts import render



class IndexView(views.TemplateView):
    template_name = 'index.html'

