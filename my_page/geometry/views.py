from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Rectangle rectangle {width}x{height} is {width * height} ')


def get_square_area(request, width: int):
    return HttpResponse(f'Square square {width}x{width} is {width ** 2} ')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Square circle radius {radius} is {pi * radius * radius} ')


def get_figure_area(request, figure, width, height=None):
    if height:
        redirect_url = reverse(figure, args=(width, height))
        return HttpResponseRedirect(redirect_url)
    redirect_url = reverse(figure, args=(width, ))
    return HttpResponseRedirect(redirect_url)
