from django.db import models
from django.contrib.auth.models import User


def custom_upload_to(instance, filename):
    print ("custom_upload")
    print ("Imprimiendo el archivo", filename)
    try:
        old_instance = Prenda.objects.get(pk=instance.pk)
        print ("Imprimiendo el archivo a borrar", old_instance.pk)
        old_instance.imagen.delete()

    except:
        pass
    return 'productos/' + filename

class Producto(models.Model):

    CATEGORIAS = (
        ("Abarrotes", "Abarrotes"),
        ("Farmacia", "Farmacia"),
        ("Electronica", "Electrónica"),
    )

    id = models.AutoField(primary_key=True, verbose_name = 'id')
    nombre = models.CharField(max_length=200, verbose_name = "Nombre")
    descripcion = models.CharField(max_length=200, verbose_name = "Descripción", null=True, blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio')
    
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name = 'Categoria')    

    cantidad = models.PositiveSmallIntegerField(verbose_name='cantidad', null=True, blank=True)
    imagen = models.ImageField(upload_to=custom_upload_to, verbose_name="imagen", null=True, blank=True)

    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'usuario')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['creado']

    def __str__(self):
        return '{} {}'.format(self.nombre, self.precio)

    # @property
    # def get_imagen_url(self):
    #     if self.imagen and hasattr(self.imagen, 'url'):
    #         return self.imagen.url
    #     else:
    #         return "/static/ropa/img/no-prenda.svg"




# class Orden(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name = 'id')

#     producto = models.ForeignKey(Producto, verbose_name = 'Producto', related_name='get_orden', on_delete = models.CASCADE)


#     tipoDeOperacion 


#     equipo_id = models.ForeignKey(Equipo, verbose_name = 'Equipo', related_name='get_boleto', on_delete = models.CASCADE)
#     tienda_id = models.ForeignKey(Tienda, verbose_name = 'Tienda', related_name='get_boleto', on_delete = models.CASCADE)


#     def __str__(self):
#         return '{} {}'.format(self.nombre, self.precio)

# class Operacion(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name = 'id')

#     comprador = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'usuario')


#     def __str__(self):
#         return '{} {}'.format(self.nombre, self.precio)

    