
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
    path(
        route = '/lista_dispositivos',
        view = views.CategoryListView.as_view(),
        name='lista_dispositivos'
    ),
    path(
        route = 'lista_dispositivos/<slug:pk>',
        view = views.DispositivoListView.as_view(),
        name='detail'
    ),
    path(
        route = '/agregar/<slug:pk>',
        view = views.CreateDispositivo_atributo.as_view(),
        name='terminar'
    ),

]
