

from django import forms

from Homologaciones.models import Homologacion, pais, referencia


class  ReferenciaForms(forms.ModelForm):

    class Meta:

        model = referencia
        fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'fabricante']
        #fields= ['profile', 'document',  'tipo', 'resultado']

class  HomologacionForm(forms.ModelForm):

    class Meta:

        model = Homologacion
        #fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'estado', 'tipo', 'fabricante']
        fields= ['profile', 'refer', 'document',  'tipo', 'resultado']

class  paisForm(forms.ModelForm):

    class Meta:

        model = pais
        fields= ['pais',]
