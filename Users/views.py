from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from  django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.decorators.cache import cache_control, never_cache
from django.views.generic import TemplateView, DetailView
from django.db.utils import IntegrityError
from Users.models import Profile
from  django.db import models
from django.contrib.auth.models import User
from Users.forms import ProfileForm, SignupForm
from  django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import views as auth_views

# class LoginView(auth_views.LoginView):
#     template_name = 'Users/login.html'
@never_cache
def login_view(request):


    if request.user.is_authenticated:
        redirect("Homologaciones:home")
        pass

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Homologaciones:home')
            pass
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)

        if user:
            print ('llego')
            login(request, user)
            return redirect('Homologaciones:home')
        else:
            pass
            return render(request, 'Users/login.html', context={'error' : 'invalid username and password'})
    return render(request, 'Users/login.html')


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass
