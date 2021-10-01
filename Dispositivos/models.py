from django.db import models
from  django.contrib.auth.models import User
from Atributos.models import atributo
from Users.models import Profile

class dispositivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    name =models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class dispositivo_atributo(models.Model):
    id_dispositivo=models.ForeignKey(dispositivo,on_delete=models.CASCADE)
    id_atributo=models.ForeignKey(atributo,on_delete=models.CASCADE)
