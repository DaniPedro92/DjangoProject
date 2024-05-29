from django.urls import path
from registro import views

app_name = 'registro'

urlpatterns = [
    path('registrar/', views.registrar_pessoa, name='registration'),
    path('lista/', views.lista_pessoas, name='lista_pessoas'),
    path('signup/', views.signup, name='signup')
]

