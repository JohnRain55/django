from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from dataclasses import dataclass
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries':
        {'description': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'types': 'fire',
         'day_start': 21,
         'month_start': [3, 31],
         'day_finish': 20,
         'month_finish': 4
         },
    'taurus':
        {'description': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'types': 'earth',
         'day_start': 21,
         'month_start': [4, 30],
         'day_finish': 21,
         'month_finish': 5
         },
    'gemini':
        {'description': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'types': 'air',
         'day_start': 22,
         'month_start': [5, 31],
         'day_finish': 21,
         'month_finish': 6
         },
    'cancer':
        {'description': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'types': 'water',
         'day_start': 22,
         'month_start': [6, 30],
         'day_finish': 22,
         'month_finish': 7
         },
    'leo':
        {'description': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'types': 'fire',
         'day_start': 23,
         'month_start': [7, 31],
         'day_finish': 21,
         'month_finish': 8
         },
    'virgo':
        {'description': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'types': 'earth',
         'day_start': 22,
         'month_start': [8, 31],
         'day_finish': 23,
         'month_finish': 9
         },
    'libra':
        {'description': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'types': 'air',
         'day_start': 24,
         'month_start': [9, 30],
         'day_finish': 23,
         'month_finish': 10
         },
    'scorpio':
        {'description': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'types': 'water',
         'day_start': 24,
         'month_start': [10, 31],
         'day_finish': 22,
         'month_finish': 11
         },
    'sagittarius':
        {'description': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'types': 'fire',
         'day_start': 23,
         'month_start': [11, 30],
         'day_finish': 22,
         'month_finish': 12
         },
    'capricorn':
        {'description': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'types': 'earth',
         'day_start': 23,
         'month_start': [12, 31],
         'day_finish': 20,
         'month_finish': 1
         },
    'aquarius':
        {'description': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'types': 'air',
         'day_start': 21,
         'month_start': [1, 31],
         'day_finish': 19,
         'month_finish': 2
         },
    'pisces':
        {'description': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'types': 'water',
         'day_start': 20,
         'month_start': [2, 29],
         'day_finish': 20,
         'month_finish': 3
         }
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
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description.get('description'),
        'sing': sign_zodiac.title(),
        'my_int': 12,
        'my_float': 123.5,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3, 4, 5),
        'my_dict': {'name': 'Lox', 'age': 59},
        'my_class': Person("Pidr", 228)
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_type_zodiac(request):
    zodiac_values = list(zodiac_dict.values())
    zodiac_types = ''
    for i in range(len(zodiac_values) - 1):
        if zodiac_values[i]['types'] not in zodiac_types:
            redirect_path = reverse('horoscope-type', args=[zodiac_values[i]['types']])
            zodiac_types += f"<li> <a href='{redirect_path}'>{zodiac_values[i]['types']} </a> </li>"
    response = f"""
        <ul>
            {zodiac_types}
        </ul>
        """
    return HttpResponse(response)


def get_element_zodiac(request, element: str):
    zodiac_elements = list(zodiac_dict.items())
    type_elements = ''
    for i in zodiac_elements:
        if i[1].get('types') == element:
            redirect_path = reverse('horoscope-name', args=[i[0]])
            type_elements += f"<li> <a href='{redirect_path}'> {i[0].title()} </a> </li>"
    if len(type_elements) < 1:
        return HttpResponseNotFound(f'Нет такой стихии {element}')
    response = f"""
        <ul>
            {type_elements}
        </ul>
        """
    return HttpResponse(response)


def get_element_zodiac_by_date(request, month: int, day: int):
    zodiac_elements = list(zodiac_dict.items())
    zodiac = ''
    for i in zodiac_elements:
        if i[1].get('month_start')[0] == month and i[1].get('day_start') <= day <= i[1].get('month_start')[1]:
            zodiac += i[0]
        elif i[1].get('month_finish') == month and 1 <= day <= i[1].get('day_finish'):
            zodiac += i[0]
    if not zodiac:
        return HttpResponseNotFound(f'Нет такой даты {month}.{day}')
    redirect_url = reverse('horoscope-name', args=(zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату {sign_zodiac}')
