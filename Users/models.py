from django.db import models
from django.contrib.auth.models import User
from Fabricantes.models import pais
# Create your models here.

class Profile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
#       country = models.ForeignKey("Homologaciones.pais", on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(pais, on_delete=models.CASCADE, null=True)
    phone_number= models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='user/pictures',
        blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
