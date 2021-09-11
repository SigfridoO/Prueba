from rest_framework import serializers

from django.contrib.auth.models import User
from registrousuarios.models import Profile
from productos.models import Producto


from rest_framework.pagination import PageNumberPagination


class CurrentUserSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileSerializer (serializers.ModelSerializer):

    user = CurrentUserSerializer(many = False)
  
    class Meta:
        model = Profile
        fields = ['avatar', 'link', 'biografia', 'user', 'saldo']


class ProductoSerializer(serializers.ModelSerializer):

    #susuario = CurrentUserSerializer(many = True)

    #usuario = serializers.SerializerMethodField('_user')
    # Create a custom method field
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'categoria', 'cantidad', 'imagen', 'usuario', )

    # def create(self, validated_data):
    #     print ('0DEntro de producto')
    #     producto = ProductoSerializer(
    #         usuario=self.context['request'].user
    #     )
    #     producto.save()
    #     return producto