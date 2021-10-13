
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
        view = views.Createpais.as_view(),
        name='new'
    ),
    path(
        route = 'consultar/<slug:pk>',
        view = views.HomologacionListView.as_view(),
        name='detail'
    ),
    # path(
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
