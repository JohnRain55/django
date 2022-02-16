from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def get_info_about_number(request, day: int):
    if 0 < day < 8:
        return HttpResponse(f'Today is {day} day of week')
    else:
        return HttpResponse(f'Number of day is not correct - {day}')


def get_info_about_day(request, day: str):
    if day == "monday":
        return HttpResponse("Jerk off")
    elif day == "tuesday":
        return HttpResponse("Be slave")
    else:
        return HttpResponseNotFound(f"Не знаю, что тебе делать в {day}")
