from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView

from .models import Club, Concept, Contact

# Create your views here.


class ClubView(ListView):
    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubView, self).get_context_data(**kwargs)
        context['title'] = settings.TITLE
        return context