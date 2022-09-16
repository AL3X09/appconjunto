from sre_parse import State
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from .models import NoticiaModel
from .serializer import NoticiaSerializer 



class NoticiaListView(generics.ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return NoticiaModel.objects.filter(is_active = True)

class NoticiaInactivaListView(generics.ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return NoticiaModel.objects.filter(is_active = False)

class NoticiaCreateView(generics.CreateAPIView):
    serializer_class = NoticiaSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Noticia guradada correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NoticiaDetailView(generics.RetrieveAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class NoticiaDeleteView(generics.DestroyAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            conjunto = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if conjunto:
                conjunto.is_active = False
                conjunto.save()
                return Response({"mensaje" : "Noticia eliminada correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class NoticiaUpdateView(generics.UpdateAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self,pk):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                conjunto_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(conjunto_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                conjunto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if conjunto_serializer.is_valid():
                    conjunto_serializer.save()
                    return Response(conjunto_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
