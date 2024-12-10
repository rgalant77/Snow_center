from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def snowboard(request):
    return HttpResponse("Vista snowboard")

def ski(request):
    return HttpResponse("Vista ski")

def antiparras(request):
    return HttpResponse("Vista antiparras")

