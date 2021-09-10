from productos.models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer