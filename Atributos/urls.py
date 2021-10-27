
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
]
