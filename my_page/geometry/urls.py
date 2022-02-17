from django.urls import path
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle'),
    path('get_<figure>_area/<int:width>/<int:height>/', views.get_figure_area),
    path('get_<figure>_area/<int:width>/', views.get_figure_area),
    path('square/<int:width>/', views.get_square_area, name='square'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle')
]