from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    readonly_fileds = ('creado', 'modificado')

    list_display = ('nombre', 'precio', 'categoria')
    ordering = ('nombre', 'categoria')
    search_fields = ('nombre', 'categoria')
    date_hierarchy = 'creado'
    list_filter = ('categoria',)

admin.site.register(Producto, ProductoAdmin)
