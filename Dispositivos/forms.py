
from django import forms

from Dispositivos.models import dispositivo


class  DispositivoForm(forms.ModelForm):

    class Meta:

        model = dispositivo
        fields= ['profile','name', 'descripcion']
