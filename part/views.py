from django.shortcuts import render
from .models import Bed
from .models import Bath
from .models import Livingroom
from .models import Kitchen
from .models import Door
from .models import Dressroom
from .models import Veranda

def bed(request):
    bed = Bed.objects
    return render(request, 'bed.html', {'beds':bed})

def bath(request):
    bath = Bath.objects
    return render(request, 'bath.html', {'baths':bath})

def livingroom(request):
    livingroom = Livingroom.objects
    return render(request, 'livingroom.html', {'livingrooms':livingroom})

def kitchen(request):
    kitchen = Kitchen.objects
    return render(request, 'kitchen.html', {'kitchens':kitchen})

def door(request):
    door = Door.objects
    return render(request, 'door.html', {'doors':door})

def dressroom(request):
    dressroom = Dressroom.objects
    return render(request, 'dressroom.html', {'dressrooms':dressroom})

def veranda(request):
    veranda = Veranda.objects
    return render(request, 'veranda.html', {'verandas':veranda})