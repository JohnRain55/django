from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


day_dict = {
    'monday': 'Jerk off', 'tuesday': 'Be slave', 'wednesday': 'Kick ass', 'thursday': 'Fap oil', 'friday': 'Bee gay',
    'saturday': 'Shabbat', 'sunday': 'Suck dicks'
}


def get_info_about_number(request, day: int):
    day_week = list(day_dict)
    if day > len(day_dict):
        return HttpResponseNotFound(f'Number of day is not correct - {day}')
    day_job = day_week[day - 1]
    redirect_url = reverse('week-day', args=(day_job, ))
    return HttpResponseRedirect(redirect_url)


def get_info_about_day(request, day: str):
    description = day_dict.get(day, None)
    if description:
        return HttpResponse(f'{description}')
    return HttpResponseNotFound(f"Не знаю, что тебе делать в {day}")
