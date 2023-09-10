from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombres', 'apellidos', 'estado')
    list_filter = ('estado',)
    search_fields = ('rut', 'nombres', 'apellidos')
    list_per_page = 20

admin.site.register(Usuario, UsuarioAdmin)