from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('info',views.info,name='information'),
    path('logoutuser',views.logoutuser,name='LogOut'),
    path('measurements',views.measurements,name='measurements'),
    path('wellbeing',views.wellbeing,name='wellbeing'),
    path('psychologyadjustment',views.psychologyadjustment,name='psychologyadjustment'),
    path('stress',views.stress,name='stress'),
    path('anxiety',views.anxiety,name='anxiety'),
]