

from django import forms
from django.forms import modelformset_factory

from Homologaciones.models import Homologacion, pais, referencia, atributo_elemento_h


class  ReferenciaForms(forms.ModelForm):

    class Meta:

        model = referencia
        fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'fabricante']
        #fields= ['profile', 'document',  'tipo', 'resultado']

class  HomologacionForm(forms.ModelForm):

    class Meta:

        model = Homologacion
        #fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'estado', 'tipo', 'fabricante']
        fields= ['profile', 'refer',  'tipo', 'resultado']

class  HomologacionUpdateForm(forms.ModelForm):

    class Meta:

        model = Homologacion
        #fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'estado', 'tipo', 'fabricante']
        fields= ['tipo', 'resultado']

class  atributo_elemento_hForm(forms.ModelForm):

    class Meta:

        model = atributo_elemento_h
        #fields= ['profile','id_dispositivo', 'refer', 'pais', 'name',  'document',  'estado', 'tipo', 'fabricante']
        fields= ['atributo', 'Homologacion',  'valor', 'document']

class  paisForm(forms.ModelForm):

    class Meta:

        model = pais
        fields= ['pais',]
