from django.contrib import admin
from django.urls import path
from unicodedata import name

from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<short_name>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKw.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('registrar-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]
