from django.urls import path
from .views import SolicitudDePedidoView

urlpatterns=[
    path('pedidos/', SolicitudDePedidoView.as_view(), name='SolicitudDePedidos_Lista'),
    path('pedidos/<int:id>', SolicitudDePedidoView.as_view(), name='SolicitudDePedidos_Proceso')
]