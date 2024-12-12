from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "productos/inicio.html")

def snowboard(request):
    return render(request, "productos/snowboard.html")

def ski(request):
    return render(request, "productos/ski.html")

def antiparras(request):
    return render(request, "productos/antiparras.html")

