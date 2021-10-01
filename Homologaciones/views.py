from django.shortcuts import render, redirect
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.mixins import  LoginRequiredMixin
# from post.models import Post
# from post.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from Homologaciones.models import Homologacion, pais, fabricante, tipo, referencia
from Homologaciones.forms import paisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from Dispositivos.models import dispositivo as dispositivo_id
# Create your views here.

@login_required()
def home(request):
    return render(request, 'Homologaciones/home.html')

@login_required()
def homologaciones(request):

    return render(request, 'Homologaciones/homologaciones.html')

class CategoryListView(ListView):
    model = Homologacion
    template_name = 'Homologaciones/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista homologaciones'
        return context

class Createreferencia(LoginRequiredMixin,SuccessMessageMixin, CreateView):

    model = referencia
    fields = [ 'profile','id_dispositivo', 'refer', 'pais', 'name',  'fabricante']
    template_name = 'Homologaciones/new4.html'
    print("holaaaaaaa")


    def form_valid(self, form):
        print("holiiiiiiiii")
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        print(form)
        form.save()
        messages.success(self.request, 'Form submission successful')
        return super(Createreferencia, self).form_valid(form)

    def get_success_url(self):

        return reverse('Homologaciones:home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fabricantes'] = queryset=fabricante.objects.all()
        context['dispositivos'] = queryset=dispositivo_id.objects.all()
        return context

# class CreateHomologacion(LoginRequiredMixin,SuccessMessageMixin, CreateView):
#
#     model = Homologacion
#     fields = [ 'profile','id_dispositivo', 'refer', 'pais', 'name',  'document', 'tipo', 'fabricante']
#     template_name = 'Homologaciones/new.html'
#     print("holaaaaaaa")
#
#
#     def form_valid(self, form):
#         print("holiiiiiiiii")
#         form.instance.user = self.request.user
#         form.instance.profile = self.request.user.profile
#         print(form)
#         form.save()
#         messages.success(self.request, 'Form submission successful')
#         return super(CreateHomologacion, self).form_valid(form)
#
#     def get_success_url(self):
#
#         return reverse('Homologaciones:home')
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tipos'] = queryset=tipo.objects.all()
#         context['fabricantes'] = queryset=fabricante.objects.all()
#         context['dispositivos'] = queryset=dispositivo_id.objects.all()
#         return context

class Createpais(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = pais
    fields = [ 'pais',]
    template_name = 'Homologaciones/new3.html'

    def form_valid(self, form):
        print("holiiiiiiiii")

        # form.instance.User = self.request.User
        # print(self.request.User)
        form.save()
        messages.success(self.request, 'Form submission successful')
        return super(Createpais, self).form_valid(form)

    def get_success_url(self):
        return reverse('Homologaciones:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paises'] = queryset=pais.objects.all()
        return context
