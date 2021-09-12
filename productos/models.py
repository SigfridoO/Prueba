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
    nombre = models.CharField(max_length=200, verbose_name = "Nombre del producto")
    descripcion = models.CharField(max_length=200, verbose_name = "Descripción", null=True, blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio')
    
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name = 'Categoria')    

    cantidad = models.PositiveSmallIntegerField(verbose_name='cantidad', null=True, blank=True)
    imagen = models.ImageField(upload_to=custom_upload_to, verbose_name="imagen", null=True, blank=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'usuario')

    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['creado']

    def __str__(self):
        return '{} {}'.format(self.nombre, self.precio)


