

from django import forms

from Homologaciones.models import Homologacion, pais


class  HomologacionForm(forms.ModelForm):

    class Meta:

        model = Homologacion
        #fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'estado', 'tipo', 'fabricante']
        fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'tipo', 'fabricante']

class  paisForm(forms.ModelForm):

    class Meta:

        model = pais
        fields= ['pais',]
