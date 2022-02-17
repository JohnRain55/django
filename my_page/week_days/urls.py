from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.get_info_about_number),
    path('<str:day>/', views.get_info_about_day, name='week-day'),
]
