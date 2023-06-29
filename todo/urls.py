from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_tarefas),
    path('add/', views.inserir_tarefa),
]