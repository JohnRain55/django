from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def get_info_about_day(request, day):
    if day == "monday":
        return HttpResponse("Jerk off")
    elif day == "tuesday":
        return HttpResponse("Be slave")
    else:
        return HttpResponseNotFound(f"Не знаю, что тебе делать в {day}")
