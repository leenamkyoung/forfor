from django.shortcuts import render
from .models import Twenty
from .models import Thirty
from .models import Forty

def twenty(request):
    twenty = Twenty.objects
    return render(request, 'twenty.html', {'twentys':twenty})

def thirty(request):
    thirty = Thirty.objects
    return render(request, 'thirty.html', {'thirtys':thirty})

def forty(request):
    forty = Forty.objects
    return render(request, 'forty.html', {'fortys':forty})