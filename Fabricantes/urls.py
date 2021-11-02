
from django.urls import path
from django.views.generic import TemplateView

# View
from Fabricantes import views


urlpatterns = [
        path(
            route = 'nuevo_fabricante',
            view = views.CreateFabricante.as_view(),
            name='nuevo_fabricante'
        ),
        path(
            route = '',
            view = views.home,
            name='fabricantes'
        ),
        path(
            route = 'lista_fabricantes',
            view = views.CategoryListView.as_view(),
            name='lista_fabricantes'
        ),
        path(
            route = 'lista_fabricantes_pais/<slug:pk>',
            view = views.FabricanteDetailView.as_view(),
            name='lista_fabricantes_pais'
        ),
        path(
            route = 'Update/<slug:pk>',
            view = views.FabricantePaisUpdate.as_view(),
            name='Update_fabricante'
        ),
]
