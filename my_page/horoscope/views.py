from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sing in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sing])
        li_elements += f"<li> <a href='{redirect_path}'>{sing.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f"This is no {sign_zodiac} in zodiac")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}<h2/>')
    return HttpResponseNotFound(f"Брат, я не ебу шо такое {sign_zodiac}")
