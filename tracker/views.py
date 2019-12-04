from django.http import HttpResponse
from django.shortcuts import render

from .models import Squirrel

def sightings(request):
    text = ''
    sightings = Squirrel.objects.all()
    context = {
        'sightings':sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def sighting_details(request, unique_squirrel_ID):
    squirrel = Squirrel.objects.get(id=unique_squirrel_ID)
    return HttpReponse(squirrel.unique_squirrel_ID)
# Create your views here.
