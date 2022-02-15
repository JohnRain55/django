from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def leo(request):
    return HttpResponse("Dick")


def scorpio(request):
    return HttpResponse("Scorpions lets celebrate and suck some dicks")


def aries(request):
    return HttpResponse("Aries lets celebrate and suck some dicks")


def taurus(request):
    return HttpResponse("Taurus lets celebrate and suck some dicks")

