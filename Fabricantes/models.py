from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class pais(models.Model):
    pais = models.CharField(max_length=50, blank=False, primary_key=True)
    capital=models.CharField(max_length=50,null=True)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pais
class fabricante(models.Model):
    fabricante = models.CharField(max_length=50, blank=False, primary_key=True)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fabricante


class fabricante_pais(models.Model):
    fabricante=models.ForeignKey(fabricante, on_delete=models.CASCADE)
    pais=models.ForeignKey(pais, on_delete=models.CASCADE)
    representante=models.CharField(max_length=200, blank=False, null=True)
    numero=PhoneNumberField( null=True, blank=False)
    email=models.EmailField(null=True, blank=False)

    def __str__(self):
        return (str(self.fabricante)+" "+str(self.pais))
