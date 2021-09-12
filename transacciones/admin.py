from django.contrib import admin
from .models import Transaccion

# Register your models here.


class TransaccionAdmin(admin.ModelAdmin):
    readonly_fileds = ('creado', 'modificado')


admin.site.register(Transaccion, TransaccionAdmin)
