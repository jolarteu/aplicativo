from django.db import models
from django.contrib.auth.models import User
from Dispositivos.models import dispositivo, dispositivo_atributo
from Users.models import Profile
from django.db.models.signals import post_save
from Fabricantes.models import fabricante, pais



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

    def __str__(self):
        return (str(self.refer)+"_"+str(self.pais))

    def get_object(self):
        #obj= Homologacion.objects.filter(refer=self.pk).order_by('-id')
        obj= str(Homologacion.objects.filter(refer=self.pk).order_by('-id')[0].estado)

        return obj

class Homologacion(models.Model):
    refer=models.ForeignKey(referencia, null=True,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    estado=models.ForeignKey(estado,  default="En curso", on_delete=models.CASCADE)
    resultado=models.ForeignKey(resultado, default="Sin terminar", on_delete=models.CASCADE )
    tipo=models.ForeignKey(tipo, default="", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.refer)+"_"+str(self.pk)

    def get_object(self):

        referencia_b=referencia.objects.filter(id_referencia=self.refer.pk).first().id_dispositivo

        try:
            atributo_b=dispositivo_atributo.objects.filter(id_atributo=7, id_dispositivo=referencia_b)[0]
        except :
            return ""
        #
        # #obj= Homologacion.objects.filter(refer=self.pk).order_by('-id')

        try:
            obj= str(atributo_elemento_h.objects.filter(Homologacion=self.pk, atributo=atributo_b).last().valor)
        except:
            obj=""

        return obj

class atributo_elemento_h(models.Model):
    atributo=models.ForeignKey(dispositivo_atributo, on_delete=models.CASCADE)
    Homologacion=models.ForeignKey(Homologacion, on_delete=models.CASCADE)
    valor=models.CharField(max_length=200, blank=True)
    document= models.FileField(upload_to='homologacion/files', blank=True)
    profile= models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.atributo)+": "+str(self.valor)


def crear_homologacion(sender, instance, **kwargs):
    profile=instance.profile
    refer=instance.refer


#
# class HistorialHomologaciones(Homologacion):
#     id_homoloacion = models.ForeignKey(Homologacion, on_delete=models.CASCADE, related_name='+')
#
#     class Meta:
#         ordering = ['-pk']

# Create your models here.
