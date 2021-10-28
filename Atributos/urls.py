
from django.urls import path
from django.views.generic import TemplateView

# View
from Atributos import views


urlpatterns = [
        path(
            route = '',
            view = views.home,
            name='caracteristicas'
        ),
        path(
            route = '/nueva_caracteristica',
            view = views.CreateCaracteristica.as_view(),
            name='nueva_caracteristica'
        ),
        path(
            route = '/lista_caracteristicas',
            view = views.CategoryListView.as_view(),
            name='lista_caracteristicas'
        ),
]
