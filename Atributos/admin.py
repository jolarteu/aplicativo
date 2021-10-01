from django.contrib import admin
from Atributos.models import atributo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import  User
# Register your models here.


@admin.register(atributo)
class  AtributosAdmin(admin.ModelAdmin):


    list_display =('id', 'name', 'descripcion', 'Obligatorio' ,'status_activo')

    # list_display_links = ('pk')

    list_editable=('name', 'descripcion', 'Obligatorio' ,'status_activo')

    # search_fields=('title')

#    list_filter = ('created', 'modified')
