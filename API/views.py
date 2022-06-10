import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import SolicitudDePedido
import json

# Create your views here.

class SolicitudDePedidoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if (id>0):
            pedidos = list(SolicitudDePedido.objects.filter(id=id).values())
            if len(pedidos)>0:
                pedido = pedidos[0]
                datos={'mensaje': "Exito", 'pedido':pedido}
            else:
                datos={'mensaje': "Pedido no encontrado ..."}
            return JsonResponse(datos)
        else:
            pedidos = list(SolicitudDePedido.objects.values())
            if len(pedidos)>0:
                datos={'mensaje': "Exito", 'pedidos':pedidos}
            else:
                datos={'mensaje': "Pedidos no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        SolicitudDePedido.objects.create(id_Pedido=jd['id_Pedido'],NombreProducto=jd['NombreProducto'],Cantidad=jd['Cantidad'])
        datos={'mensaje': "Exito"}
        return JsonResponse(datos)

    def put(self, request,id):
        jd = json.loads(request.body)
        pedidos = list(SolicitudDePedido.objects.filter(id=id).values())
        if len(pedidos)>0:
            pedido = SolicitudDePedido.objects.get(id=id)
            pedido.id_Pedido = jd['id_Pedido']
            pedido.NombreProducto = jd['NombreProducto']
            pedido.Cantidad = jd['Cantidad']
            pedido.save()
            datos={'mensaje': "Exito"}
        else: 
            datos={'mensaje': "Pedido no encontrado ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        pedidos = list(SolicitudDePedido.objects.filter(id=id).values())
        if len(pedidos)>0:
            SolicitudDePedido.objects.filter(id=id).delete()
            datos={'mensaje': "Exito"}
        else:
            datos={'mensaje': "Pedido no encontrado ..."}
        return JsonResponse(datos)
