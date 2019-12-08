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

def update(request, unique_squirrel_ID):
    squirrel = Squirrel.objects.get(unique_squirrel_ID = unique_squirrel_ID)
    if request.method == 'POST':
        # check data with form
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_ID}')
    else:
        # build empty form
        form = SquirrelForm(instance = squirrel)
    context = {
        'form': form,
    }
    return render(request, 'tracker/update.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'tracker/map.html', context)
# Create your views here.
