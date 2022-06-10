from django.db import models

# Create your models here.

class SolicitudDePedido(models.Model):
    id_Pedido = models.PositiveIntegerField()
    NombreProducto = models.CharField(max_length=35)
    Cantidad = models.PositiveSmallIntegerField()