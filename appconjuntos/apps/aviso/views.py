from typing import OrderedDict
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from .models import AvisoModel
from .serializer import AvisoSerializer

class AvisoSinAprobarListView(generics.ListAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return AvisoModel.objects.filter(is_active = True).filter(is_approved = False)
        
class AvisoAprobadosListView(generics.ListAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return AvisoModel.objects.filter(is_active = True).filter(is_approved = True)

class AvisoVentaListView(generics.ListAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return AvisoModel.objects.filter(is_active = True).filter(is_approved = True).filter(fk_tipoaviso = 1)

class AvisoArriendoListView(generics.ListAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return AvisoModel.objects.filter(is_active = True).filter(is_approved = True).filter(fk_tipoaviso = 2)

class AvisoPortafolioListView(generics.ListAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return AvisoModel.objects.filter(is_active = True).filter(is_approved = True).filter(fk_tipoaviso = 3)

class AvisoCreateView(generics.CreateAPIView):
    serializer_class = AvisoSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Aviso guradado correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AvisoDetailView(generics.RetrieveAPIView):
    serializer_class = AvisoSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class AvisoDeleteView(generics.DestroyAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            propiedad = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if propiedad:
                propiedad.is_active = False
                propiedad.save()
                return Response({"mensaje" : "Aviso eliminado correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class AvisoUpdateView(generics.UpdateAPIView):
    serializer_class = AvisoSerializer

    def get_queryset(self,pk):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                propiedad_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(propiedad_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                propiedad_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if propiedad_serializer.is_valid():
                    propiedad_serializer.save()
                    return Response(propiedad_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)