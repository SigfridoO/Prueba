from django.db import models
from django.contrib.auth.models import User

def custom_upload_to(instance, filename):

    print ("Imprimiendo el archivo", filename)
    try:
        old_instance = Profile.objects.get(pk=instance.pk)
        print ("Imprimiendo el archivo a borrar", old_instance.pk)
        old_instance.avatar.delete()
    except:
        pass
    return 'profiles/' + filename

class Profile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name = 'id')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank =True)
    # TODO:
    saldo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Saldo', default=1000)

    # creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    # modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')


    class Meta:
        verbose_name = "perfil de usuario"
        verbose_name_plural = "perfiles de usuario"
        ordering = ['user']
