from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_carros, name='listar_carros'),
    path('carro/novo/', views.criar_carro, name='criar_carro'),
    path('carro/editar/<int:pk>/', views.editar_carro, name='editar_carro'),
    path('carro/deletar/<int:pk>/', views.deletar_carro, name='deletar_carro'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reserva/novo/', views.criar_reserva, name='criar_reserva'),
]
