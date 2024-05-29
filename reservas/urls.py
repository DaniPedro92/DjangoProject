from django.urls import path
from reservas import views as reservas_views
from django.contrib.auth import views as auth_views 

app_name = 'reservas'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='reservas/login.html'), name='login'),
    path('fazer_reserva/', reservas_views.fazer_reserva, name='fazer_reserva'),
    path('lista_reservas/', reservas_views.lista_reservas, name='lista_reservas'),
]
