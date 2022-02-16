from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == "leo":
        return HttpResponse("Leo like suck dicks")
    elif sign_zodiac == "scorpio":
        return HttpResponse("Scorpions lets celebrate and suck some dicks")
    elif sign_zodiac == "aries":
        return HttpResponse("Aries == suckers ")
    elif sign_zodiac == "taurus":
        return HttpResponse("Taurus bee my slave")
    else:
        return HttpResponseNotFound(f"Брат, я не ебу шо такое {sign_zodiac}")
