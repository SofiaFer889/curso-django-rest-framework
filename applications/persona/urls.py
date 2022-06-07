from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('listar-todo-empleados', views.ListAllEmpleados.as_view()),
    path('lista-by-area/<shorname>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades-empleado', views.ListHabilidadesHempleados.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('add-empleado', views.EmpleadoCreateView.as_view()),
    path('success', views.SuccessView.as_view(), name='correcto')
]