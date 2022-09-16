from xml.dom import ValidationErr
from rest_framework import serializers
from .models import ConjuntoModel

class ConjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjuntoModel
        fields = '__all__'
        #fields = ('Nombre','email','telephone', 'logo', ('imagen'[69:100]), 'adress', 'about', 'eslogan', 'is_active') not funciona

class ConjuntoNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjuntoModel
        fields = ('id','name','logo',)


"""class TestConjuntoSerializer (serializers.Serializer):
    name = serializers.CharField( max_length = 255)
    email = serializers.EmailField(max_length = 255)
    telephone = serializers.CharField( max_length = 10)
    #logo = serializers.ImageField(upload_to ='img/conjunto/')
    #Imagen = serializers.ImageField( upload_to ='img/conjunto/')
    adress = serializers.CharField(max_length = 255)
    is_active = serializers.BooleanField(default = True)

    #Agreguo las validaciones personalizadas o sebrescribir las validaciones
    def validate_name(self, value):
        if value ==  '':
            raise serializers.ValidationError('el campo es obligatorio y no puede estar vacio ')
        return value

    def validate_email(self, value):
        print(value)
        return value

    def validate_tephone(self, value):
        print(value)
        return value
    
    def validate_adress(self, value):
        print(value)
        return value

    def validate_is_active(self, value):
        print(value)
        return value

    def validate(self, data):
        print(data)
        return data
        """