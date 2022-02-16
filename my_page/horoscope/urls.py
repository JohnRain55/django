from django.urls import path
from . import views

urlpatterns = [
    path('leo/', views.leo),
    path(' scorpion/', views.scorpio),
    path('aries/', views.aries),
    path('taurus/', views.taurus),

]