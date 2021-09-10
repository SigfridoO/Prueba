from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fileds = ('creado', 'modificado')

    list_display = ('user', 'saldo', )
    ordering = ('user',)
    search_fields = ('user',)
    
    

admin.site.register(Profile, ProfileAdmin)

