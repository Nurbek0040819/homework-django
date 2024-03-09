from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the nurbek")

def about(request):
    return HttpResponse("Nima gapla ")

def nurbek1(request):
    return HttpResponse('Ozbekiston buyuk davlat')

def nurbek2(request):
    return HttpResponse("aasdfadfoooooooooooooo")