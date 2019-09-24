from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Sponsor


class HomeView(generic.TemplateView):
    template_name = 'project/index.html'

class CreateView(generic.TemplateView):
    template_name = 'project/create.html'

class ResetView(generic.TemplateView):
    template_name = 'project/reset.html'
