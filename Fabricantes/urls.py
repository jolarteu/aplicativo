
from django.urls import path
from django.views.generic import TemplateView

# View
from Fabricantes import views


urlpatterns = [
        path(
            route = '',
            view = views.home,
            name='fabricantes'
        ),
]
