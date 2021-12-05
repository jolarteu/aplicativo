
from django.urls import path
from django.views.generic import TemplateView

# View
from Homologaciones import views


urlpatterns = [


    path(
        route = '',
        view = views.home,
        name='home'
    ),
    path(
        route = 'homologaciones',
        view = views.homologaciones,
        name='homologaciones'
    ),


    path(
        route = 'consultar',
        view = views.CategoryListView.as_view(),
        name='consultar'
    ),
    path(
        route = 'new',
        view = views.Createreferencia.as_view(),
        name='new'
    ),
    path(
        route = 'consultar/<slug:pk>',
        view = views.HomologacionListView.as_view(),
        name='detail'
    ),
    path(
        route = 'terminar/<slug:pk>',
        view = views.Homologacion_terminar.as_view(),
        name='terminar'
    ),
    path(
        route = 'detalles_homologacion/<slug:pk>',
        view = views.detalles_homologacionDetailview.as_view(),
        name= 'detalles_homologacion'
        ),
    # path(,
    #     route = 'consultar/<slug:pk>',
    #     view = views.HomologacionDetailView.as_view(),
    #     name='detail'
    # ),
    # path(
    #     route = 'homologacion/<slug:pk>',
    #     view = views.CreateHomologacion.as_view(),
    #     name='homologacion'
    # ),
    # path(
    #     route = 'new',
    #     view = views.CreateHomologacion.as_view(),
    #     name='new'
    # ),

]
