from django.contrib import admin
from Fabricantes.models import fabricante_pais, pais, fabricante

# Register your models here.
@admin.register(fabricante_pais)
class  referenciaAdmin(admin.ModelAdmin):


    list_display =('fabricante', 'pais',  'representante', 'numero',
                    'email')


@admin.register(pais)
class  paisAdmin(admin.ModelAdmin):

    list_display =('pais', 'created')



@admin.register(fabricante)
class  fabricanteAdmin(admin.ModelAdmin):

    list_display =('fabricante', 'created')
