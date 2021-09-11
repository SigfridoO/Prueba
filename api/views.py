from .serializers import ProductoSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from productos.models import Producto
from registrousuarios.models import Profile

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class RealizarTransaccion(views.APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def  post(self, request):

        content = {
            'resultado': 'Resultado',
        }

        return Response(content)

class ObtenerPerfilUsuario(views.APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get (self, request):

        #print ("imprimiendo", request.user, request.user.email)

        # usuario = User.objects.get(email = request.user.email)
        # serializer = CurrentUserSerializer(usuario)

        # return Response(serializer.data)


        usuario = Profile.objects.get(user = request.user)
        serializer = ProfileSerializer (usuario)

        return Response(serializer.data)
        

