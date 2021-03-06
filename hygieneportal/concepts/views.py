from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.generic import ListView

from .models import Club, Concept, Contact

# Create your views here.


class ClubView(ListView):
    model = Club


def concept_view(request, concept_id:int, concept_name:str):
    concept: Concept = get_object_or_404(Concept, id=concept_id)
    for club in concept.club_set.all():
        club.access()
    return FileResponse(concept.pdf.open())