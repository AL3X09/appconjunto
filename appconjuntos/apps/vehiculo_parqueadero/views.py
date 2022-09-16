from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
#https://es.acervolima.com/como-detectar-el-cierre-del-navegador-o-la-pestana-en-javascript/
from django.core.exceptions import ObjectDoesNotExist

from .models import VehiculoParqueaderoModel
from .serializer import VehiculoParqueaderoSerializer

class VehiculoParqueaderoListView(generics.ListAPIView):
    serializer_class = VehiculoParqueaderoSerializer
    
    def get_queryset(self,fk_propiedad):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(fk_propiedad = fk_propiedad).first()
    
    #sobreescribo el metodo
    def get(self, request, fk_propiedad=None):
        try:
            if self.get_queryset(fk_propiedad):
                pedido_serializer = self.serializer_class(self.get_queryset(fk_propiedad))
                return Response(pedido_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "No existen datos"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VehiculoParqueaderoCreateView(generics.CreateAPIView):
    serializer_class = VehiculoParqueaderoSerializer
   
    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Parqueo almacenado correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VehiculoParqueaderoDetailView(generics.RetrieveAPIView):
    serializer_class = VehiculoParqueaderoSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class VehiculoParqueaderoDeleteView(generics.DestroyAPIView):
    serializer_class = VehiculoParqueaderoSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            vehiculo_parq = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if vehiculo_parq:
                vehiculo_parq.is_active = False
                vehiculo_parq.save()
                return Response({"mensaje" : "Parqueo eliminado correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class VehiculoParqueaderoUpdateView(generics.UpdateAPIView):
    serializer_class = VehiculoParqueaderoSerializer

    def get_queryset(self,pk):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                vehi_parq_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(vehi_parq_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Parqueo no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                vehi_parq_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if vehi_parq_serializer.is_valid():
                    vehi_parq_serializer.save()
                    return Response(vehi_parq_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Parqueo no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
