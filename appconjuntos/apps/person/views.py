from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from .models import PersonModel
from .serializer import PersonSerializer

class PersonListView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return PersonModel.objects.filter(is_active = True)

class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Conjunto guradado correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PersonaDetailView(generics.RetrieveAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class PersonaDeleteView(generics.DestroyAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            persona = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if persona:
                persona.is_active = False
                persona.save()
                return Response({"mensaje" : "Conjunto eliminado correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class PersonaUpdateView(generics.UpdateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self,pk):
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                persona_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(persona_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                persona_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if persona_serializer.is_valid():
                    persona_serializer.save()
                    return Response(persona_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)