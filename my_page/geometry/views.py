from django.shortcuts import render
from django.http import HttpResponse
from math import pi

# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Square rectangle {width}x{height} is {width * height} ')


def get_square_area(request, width: int):
    return HttpResponse(f'Square square {width}x{width} is {width ** 2} ')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Square circle radius {radius} is {pi * radius * radius} ')
