
from django import forms

from Fabricantes.models import fabricante


class  FabricanteForm(forms.ModelForm):

    class Meta:

        model = fabricante
        fields= ['fabricante']
