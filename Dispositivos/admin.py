from django.contrib import admin
from  Dispositivos.models import dispositivo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import  User
from  Dispositivos.models import dispositivo_atributo

# Register your models here.


@admin.register(dispositivo)
class  DispositivosAdmin(admin.ModelAdmin):


    list_display =('id', 'name', 'descripcion', 'status_activo', )

    # list_display_links = ('pk')

    list_editable=('name', 'descripcion', 'status_activo')

    # search_fields=('title')

#    list_filter = ('created', 'modified')


@admin.register(dispositivo_atributo)
class  Dispositivo_adtributoAdmin(admin.ModelAdmin):


    list_display =('id_dispositivo' , 'id_dispositivo')

    # list_display_links = ('pk')

    #list_editable=('name', 'descripcion', 'status_activo')

    # search_fields=('title')

#    list_filter = ('created', 'modified')
