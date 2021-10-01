from django.db import models
from  django.contrib.auth.models import User


class atributo(models.Model):
    id = models.BigAutoField(primary_key=True)
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    Obligatorio = models.BooleanField()
    status_activo = models.BooleanField()

    def __str__(self):
        return self.name
