from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')


urlpatterns = [
    path('<my_date:sign_zodiac>/', views.get_my_date_converters),
    path('', views.index),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:month>/<int:day>/', views.get_element_zodiac_by_date),
    path('kianu/', views.get_info_about_kianu),
    path('type/', views.get_type_zodiac),
    path('type/<str:element>/', views.get_element_zodiac, name='horoscope-type'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
