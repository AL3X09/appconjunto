from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from .models import AuditoriaPedidoModel
from .serializer import AuditoriaPedidoSerializer

class AuditoriaPedidoListView(generics.ListAPIView):
    serializer_class = AuditoriaPedidoSerializer

    def get_queryset(self):
        return AuditoriaPedidoModel.objects.filter(is_active = True)

class AuditoriaPedidoCreateView(generics.CreateAPIView):
    serializer_class = AuditoriaPedidoSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Pedido guradado correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuditoriaPedidoDetailView(generics.RetrieveAPIView):
    serializer_class = AuditoriaPedidoSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class AuditoriaPedidoDeleteView(generics.DestroyAPIView):
    serializer_class = AuditoriaPedidoSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            pedido = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if pedido:
                pedido.is_active = False
                pedido.save()
                return Response({"mensaje" : "Pedido eliminado correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class AuditoriaPedidoUpdateView(generics.UpdateAPIView):
    serializer_class = AuditoriaPedidoSerializer

    def get_queryset(self,pk):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                pedido_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(pedido_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Pedido no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                pedido_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if pedido_serializer.is_valid():
                    pedido_serializer.save()
                    return Response(pedido_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Pedido no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
