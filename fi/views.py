from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def aaa(request):
    return render(request, 'aaa.html')

