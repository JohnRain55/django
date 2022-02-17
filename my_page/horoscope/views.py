from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zodiac_dict = {
    'aries': 'Arias have good ass',
    'taurus': 'Taurus bee my slave',
    'gemini': 'Gemini your planet is Mercury, only for guys',
    'cancer': 'Cancer you know how it do ',
    'leo': 'Leo like suck dicks',
    'virgo': "Virgo is not in team",
    'libra': 'Libra take balance with dicks',
    'scorpio': 'Scorpions lets celebrate and suck some dicks"',
    'sagittarius': 'Sagittarius get you ario at correct place',
    'capricorn': 'Capricorn should fiend 300$',
    'aquarius': 'Aquarius just swim in semen',
    'pisces': 'Pisces like touch they ass'
}


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f"This is no {sign_zodiac} in zodiac")
    name_zodiac = zodiacs[sign_zodiac - 1]
    return HttpResponseRedirect(f'/horoscope/{name_zodiac}')


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Брат, я не ебу шо такое {sign_zodiac}")
