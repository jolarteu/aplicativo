
from django import forms

from Atributos.models import atributo


class  AtributoForm(forms.ModelForm):

    class Meta:

        model = atributo
        fields= ['profile','name', 'descripcion']
