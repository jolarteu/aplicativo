from django.db import models
from  django.contrib.auth.models import User
from  Dispositivos.models import dispositivo
from Users.models import Profile


class pais(models.Model):
    pais = models.CharField(max_length=50, blank=False, primary_key=True)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pais

class estado(models.Model):
    estado=models.CharField(max_length=50, blank=False, primary_key=True)
    descripcion=models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estado

class resultado(models.Model):
    resultado = models.CharField(max_length=50, blank=False, primary_key=True)
    descripcion=models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resultado

class tipo(models.Model):
    tipo = models.CharField(max_length=50, blank=False, primary_key=True)
    descripcion=models.CharField(max_length=200, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo

class fabricante(models.Model):
    fabricante = models.CharField(max_length=50, blank=False, primary_key=True)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fabricante

class referencia(models.Model):
    id_referencia = models.BigAutoField(primary_key=True)
    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    refer=models.CharField(max_length=50, blank=False)
    id_dispositivo=models.ForeignKey(dispositivo, default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pais=models.ForeignKey(pais, default="", on_delete=models.CASCADE)
    fabricante=models.ForeignKey(fabricante, default="", on_delete=models.CASCADE)
    class Meta:
        unique_together = [['refer', 'id_dispositivo', 'pais']]

class Homologacion(models.Model):
    refer=models.ForeignKey(referencia, null=True,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    document= models.FileField(upload_to='homologacion/files')
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    estado=models.ForeignKey(estado,  default="En curso", on_delete=models.CASCADE)
    resultado=models.ForeignKey(resultado, default="Sin terminar", on_delete=models.CASCADE )
    tipo=models.ForeignKey(tipo, default="", on_delete=models.CASCADE)



#
# class HistorialHomologaciones(Homologacion):
#     id_homoloacion = models.ForeignKey(Homologacion, on_delete=models.CASCADE, related_name='+')
#
#     class Meta:
#         ordering = ['-pk']

# Create your models here.
