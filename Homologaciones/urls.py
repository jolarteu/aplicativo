
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
    # path(
    #     route = 'new',
    #     view = views.CreateHomologacion.as_view(),
    #     name='new'
    # ),

]
