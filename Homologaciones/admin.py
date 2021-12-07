from django.contrib import admin
from Homologaciones.models import Homologacion, pais, estado, resultado, tipo, fabricante, referencia, atributo_elemento_h
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import  User
# Register your models here.

#
@admin.register(referencia)
class  referenciaAdmin(admin.ModelAdmin):


    list_display =('pk', 'refer', 'profile',  'name', 'created',
                    'modified','fabricante')

@admin.register(atributo_elemento_h)
class  referenciaAdmin(admin.ModelAdmin):


    list_display =('atributo', 'Homologacion',  'valor', 'document',
                    'profile')


@admin.register(Homologacion)
class  HomologacionAdmin(admin.ModelAdmin):


    list_display =('pk','refer', 'profile', 'created',
                    'modified', 'resultado', 'estado', 'tipo')

#     # list_display_links = ('pk')
#
#     list_editable=('name',  'document',
#                      'estado', 'tipo', 'fabricante')

    # search_fields=('title')

#    list_filter = ('created', 'modified')

@admin.register(estado)
class  estadoAdmin(admin.ModelAdmin):

    list_display =('estado', 'created')

@admin.register(resultado)
class  resultadoAdmin(admin.ModelAdmin):

    list_display =('resultado', 'created')

@admin.register(tipo)
class  tipoAdmin(admin.ModelAdmin):

    list_display =('tipo', 'created')
