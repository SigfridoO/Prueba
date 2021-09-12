from django.db import models
from django.utils.timezone import now
from productos.models import Producto
from django.contrib.auth.models import User
# Create your models here.

# class Orden(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name = 'id')

#     producto = models.ForeignKey(Producto, verbose_name = 'Producto', related_name='get_orden', on_delete = models.CASCADE)


#     tipoDeOperacion 


#     equipo_id = models.ForeignKey(Equipo, verbose_name = 'Equipo', related_name='get_boleto', on_delete = models.CASCADE)
#     tienda_id = models.ForeignKey(Tienda, verbose_name = 'Tienda', related_name='get_boleto', on_delete = models.CASCADE)


#     def __str__(self):
#         return '{} {}'.format(self.nombre, self.precio)

class Transaccion(models.Model):
    TIPO_DE_OPERACION = (
        ("Compra", "Compra"),
        ("Venta", "Venta"),
    )

    id = models.AutoField(primary_key=True, verbose_name = 'id')
    fecha = models.DateTimeField(verbose_name = 'fecha', default = now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'usuario', related_name='transaccion')
    producto = models.ForeignKey(Producto, verbose_name='transaccion', on_delete=models.CASCADE, related_name= 'transaccion')
    cantidad = models.PositiveSmallIntegerField(verbose_name='cantidad', null=True, blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio')
    tipoDeOperacion = models.CharField(max_length=50, choices=TIPO_DE_OPERACION, verbose_name = 'Categoria')     

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')



    class Meta:
        verbose_name = "transacción"
        verbose_name_plural = "transacciones"
        ordering = ['fecha']

    def __str__(self):
        return '{} {}'.format(self.usuario, self.producto)