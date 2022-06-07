from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print('======hola=====')

urlpatterns = [
    path('departamento', DesdeApps),
]