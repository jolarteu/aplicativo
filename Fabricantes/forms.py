
from django import forms

from Fabricantes.models import fabricante, fabricante_pais


class  FabricanteForm(forms.ModelForm):

    class Meta:

        model = fabricante
        fields= ['fabricante']


class FabricantesPaisUpdate(forms.ModelForm):

    class Meta:

        model = fabricante_pais
        fields = ['representante','numero', 'email']

class FabricantesPaisForm(forms.ModelForm):

    class Meta:

        model = fabricante_pais
        fields = ['representante','pais', 'numero', 'email']
