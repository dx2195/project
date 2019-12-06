from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Squirrel
from .forms import SquirrelForm

def sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def sighting_details(request, unique_squirrel_ID):
    squirrel = Squirrel.objects.get(id=unique_squirrel_ID)
    return HttpReponse(squirrel.unique_squirrel_ID)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'tracker/map.html', context)
# Create your views here.
