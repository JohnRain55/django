from django.urls import path
from . import views

urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about_sign_zodiac),
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
]