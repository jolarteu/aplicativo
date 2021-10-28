
from django import forms

from Dispositivos.models import dispositivo, dispositivo_atributo


class  DispositivoForm(forms.ModelForm):

    class Meta:

        model = dispositivo
        fields= ['profile','name', 'descripcion']


class  dispositivo_atributoForm(forms.ModelForm):

    class Meta:

        model = dispositivo_atributo
        fields= ['id_atributo']
