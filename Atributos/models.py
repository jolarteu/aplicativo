from django.db import models
from  django.contrib.auth.models import User
from Users.models import Profile


class atributo(models.Model):

    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    name =models.CharField(max_length=50, blank=False, unique=True)
    descripcion = models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    Obligatorio = models.BooleanField(default=True)
    status_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
