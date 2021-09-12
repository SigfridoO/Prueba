
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProductoSerializer, ProfileSerializer

from productos.models import Producto

from transacciones.models import Transaccion

from registrousuarios.models import Profile

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ObtenerPerfilUsuario(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self, request):

        print ("imprimiendo", request.user, request.user.email)

        # usuario = User.objects.get(email = request.user.email)
        # serializer = CurrentUserSerializer(usuario)

        # return Response(serializer.data)


        usuario = Profile.objects.get(user = request.user)
        serializer = ProfileSerializer (usuario)

        return Response(serializer.data)
        

class OperacionDeCompra(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



    def  post(self, request):
        #print (self.request.data)
        parametros = dict(self.request.data.lists())

        print (parametros)

        # Campos necesarios para realizar la operación 
        tipoDeOperacion =  parametros.get('operacion')
        idProducto =  parametros.get('idproducto')
        cantidad =  parametros.get('cantidad')
        # validando parametros
        try:
            if tipoDeOperacion: tipoDeOperacion=tipoDeOperacion[0]
            if idProducto: idProducto=idProducto[0]
            if cantidad: cantidad=int(cantidad[0])
        except e:
            content = {
                'error': 'Parametros incorrectos',
            }
        else:

            if tipoDeOperacion == 'compra':
                # Se obtiene el producto con el id del producto y se verifica que exista
                producto = Producto.objects.get(id=idProducto)

                if producto:
                    cantidadDisponible = producto.cantidad
                    if cantidad > 0:
                        if cantidad > cantidadDisponible:
                            content = {
                                'mensaje': 'No hay suficientes productos para realizar la compra',
                            }
                        else: # continua hay suficiente cantidad de productos
                            usuario = request.user
                            

                            if usuario != producto.usuario:  # No se puede comprar al mismo usuario


                                # Se resta la cantidad al usuario que vende el producto
                                producto.cantidad = cantidadDisponible - cantidad
                                producto.save()

                                vendedor = Profile.objects.get(user = producto.usuario)
                                comprador = Profile.objects.get(user = usuario)

                                print (tipoDeOperacion, idProducto, cantidad, usuario)
                                print ('Imprimiendo el vendedor', vendedor.user, vendedor.saldo)
                                print ('Imprimiendo el comprador', comprador.user, comprador.saldo)

                                # Se resta el saldo del usuario que hace la compra
                                # Se incrementa el saldo del usuario que vende el producto
                                vendedor.saldo += producto.precio
                                comprador.saldo -= producto.precio
                                vendedor.save()
                                comprador.save()


                                # Realizar la transacción de compra
                                transaccion = Transaccion.objects.create(usuario=comprador.user, producto=producto, cantidad=cantidad, precio=producto.precio, tipoDeOperacion='Compra' )

                                # Realizar la transacción de venta
                                transaccion = Transaccion.objects.create(usuario=vendedor.user, producto=producto, cantidad=cantidad, precio=producto.precio, tipoDeOperacion='Venta' )

                                print(transaccion)



                                print ('Imprimiendo el vendedor', vendedor.user, vendedor.saldo)
                                print ('Imprimiendo el comprador', comprador.user, comprador.saldo)
                                content = {
                                    'mensaje': 'Transacción realizada',
                                }

                            else:
                                content = {
                                    'mensaje': 'Ese producto pertenece al mismo usuario, no se puede realizar la compra',
                                }
                    else:
                        content = {
                            'mensaje': 'debe ser una cantidad valida',
                        }
                else:
                    content = {
                        'mensaje': 'Ya no existe ese producto',
                    }
            else:
                content = {
                    'error': 'No se proporciono un tipo de operación válida',
                }
        return Response(content)


 