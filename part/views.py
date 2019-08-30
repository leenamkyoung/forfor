from django.shortcuts import render, get_object_or_404
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

def detail(request, dressroom_id): #드레스룸디테일
    dressroom_detail = get_object_or_404(Dressroom, pk = dressroom_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail.html', {'dressroom':dressroom_detail})

def detail1(request, bath_id): #드레스룸디테일
    bath_detail = get_object_or_404(Bath, pk = bath_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail1.html', {'bath':bath_detail})

def detail2(request, dressroom_id): #드레스룸디테일
    bed_detail = get_object_or_404(Bed, pk = bed_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail2.html', {'bed':bed_detail})

def detail3(request, door_id): #드레스룸디테일
    door_detail = get_object_or_404(Door, pk = door_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail3.html', {'door':door_detail})

def detail4(request, kitchen_id): #드레스룸디테일
    kitchen_detail = get_object_or_404(Kitchen, pk = kitchen_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail4.html', {'kitchen':kitchen_detail})

def detail5(request, livingroom_id): #드레스룸디테일
    livingroom_detail = get_object_or_404(Livingroom, pk = livingroom_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail5.html', {'livingroom':livingroom_detail})

def detail6(request, veranda_id): #드레스룸디테일
    veranda_detail = get_object_or_404(Veranda, pk = veranda_id) #이용자가 원하는 몇번블로그 객체
    return render(request, 'detail6.html', {'veranda':veranda_detail})