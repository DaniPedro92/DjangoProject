from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.mostrar_tarefas, name='listar'),
    path('add/', views.inserir_tarefa, name='inserir'),
    path('del/<int:id>', views.eliminar_tarefa, name='eliminar'),
    path('edit/<int:id>', views.editar_tarefa, name='editar'),
]