
from django.urls import path
from django.views.generic import TemplateView

# View
from Dispositivos import views


urlpatterns = [


    path(
        route = '/nuevo_dispositivo',
        view = views.CreateDispositivo.as_view(),
        name='nuevo_dispositivo'
    ),

    path(
        route = '',
        view = views.dispositivo_v,
        name='dispositivo'
    ),

]
