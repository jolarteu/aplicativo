from django.contrib import admin
from  Homologaciones.models import Homologacion, pais, estado, resultado, tipo, fabricante
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import  User
# Register your models here.


@admin.register(Homologacion)
class  HomologacionAdmin(admin.ModelAdmin):


    list_display =('id_dispositivo', 'profile', 'refer', 'pais', 'name',  'document', 'created',
                    'modified', 'estado', 'tipo', 'fabricante')

    # list_display_links = ('pk')

    list_editable=('name',  'document',
                     'estado', 'tipo', 'fabricante')

    # search_fields=('title')

#    list_filter = ('created', 'modified')
@admin.register(pais)
class  paisAdmin(admin.ModelAdmin):

    list_display =('pais', 'created')

@admin.register(estado)
class  estadoAdmin(admin.ModelAdmin):

    list_display =('estado', 'created')

@admin.register(resultado)
class  resultadoAdmin(admin.ModelAdmin):

    list_display =('resultado', 'created')

@admin.register(tipo)
class  tipoAdmin(admin.ModelAdmin):

    list_display =('tipo', 'created')

@admin.register(fabricante)
class  fabricanteAdmin(admin.ModelAdmin):

    list_display =('fabricante', 'created')
