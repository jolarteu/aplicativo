
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# View
from Users import views


urlpatterns = [


    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

]
