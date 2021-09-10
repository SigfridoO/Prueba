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
        fields = ['avatar', 'link', 'bio', 'user', 'saldo']


class ProductoSerializer(serializers.ModelSerializer):

    usuario = CurrentUserSerializer(many = False)

    class Meta:
        model = Producto
        fields = '__all__'