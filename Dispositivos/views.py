from django.shortcuts import render
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from Dispositivos.models import dispositivo, dispositivo_atributo
from django.contrib import messages
from django.urls import reverse
from Dispositivos.forms import dispositivo_atributoForm

@login_required()
def dispositivo_v(request):

    return render(request, 'Dispositivos/dispositivo.html')


class CreateDispositivo(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = dispositivo
    fields = [ 'profile', 'name', 'descripcion']
    template_name = 'Dispositivos/new.html'

    def form_valid(self, form):
        print("holiiiiiiiii")

        # form.instance.User = self.request.User
        # print(self.request.User)
        form.save()
        messages.success(self.request, 'Form submission successful')
        return super(CreateDispositivo, self).form_valid(form)

    def get_success_url(self):
        return reverse('Homologaciones:home')

class CategoryListView(LoginRequiredMixin, ListView):
    model = dispositivo
    template_name = 'Dispositivos/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de dispositivos'
        return context


class DispositivoListView(LoginRequiredMixin, DetailView):
    model = dispositivo_atributo
    template_name = 'Dispositivos/lista_caracteristicas.html'

    queryset = dispositivo.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista caracteristicas'
        context['object_list']=dispositivo_atributo.objects.filter(id_dispositivo=self.obj.pk)
        return context


class  CreateDispositivo_atributo(DetailView, CreateView):
    model=dispositivo
    template_name= 'Dispositivos/agregar.html'
    form_class=dispositivo_atributoForm

    queryset = dispositivo.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de dispositivos'
        context['dispositivo']=self.get_object()
        return context

    def form_valid(self, form):
        print("holiiiiiiiii")
        instance= form.save(commit=False)
        instance.id_dispositivo=self.get_object()
        # form.instance.User = self.request.User
        # print(self.request.User)
        #form.save()
        instance.save()
        messages.success(self.request, 'Form submission successful')
        return super(CreateDispositivo_atributo, self).form_valid(form)

    def get_success_url(self):
        return reverse('Dispositivos:lista_dispositivos')
