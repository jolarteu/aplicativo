from django.shortcuts import render, redirect
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.forms import modelformset_factory

# from post.models import Post
# from post.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from Homologaciones.models import Homologacion, pais, fabricante, tipo, referencia, estado, resultado, atributo_elemento_h
from Homologaciones.forms import paisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from Dispositivos.models import dispositivo as dispositivo_id
from Dispositivos.models import dispositivo_atributo
from django.views.generic.edit import FormMixin
from Homologaciones.forms import  HomologacionForm, atributo_elemento_hForm, ReferenciaForms, paisForm
# Create your views here.
from django.http import HttpResponseRedirect

@login_required()
def home(request):
    return render(request, 'Homologaciones/home.html')

@login_required()
def homologaciones(request):

    return render(request, 'Homologaciones/homologaciones.html')


class CreateHomologacion(FormMixin, DetailView):
    template_name = 'Homologaciones/crear.html'
    form_class = HomologacionForm
    form_class2= atributo_elemento_hForm
    model = Homologacion


    queryset = referencia.objects.all()
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = referencia.objects.all()
    context_object_name = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = queryset=estado.objects.all()
        context['resultados'] = queryset=resultado.objects.all()

        return context

    def homologacion(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(CreateHomologacion, self).form_valid(form)


    def get_success_url(self):
        return reverse('Homologacion:home')

class HomologacionDetailView(LoginRequiredMixin, DetailView):

    template_name = 'Homologaciones/detail.html'

    queryset = referencia.objects.all()
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = referencia.objects.all()
    context_object_name = 'pk'

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atributos'] = queryset=dispositivo_atributo.objects.filter(id_dispositivo=self.obj.id_dispositivo)
        return context

class HomologacionListView(DetailView):
    model = Homologacion
    template_name = 'Homologaciones/terminar.html'

    queryset = referencia.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista homologaciones'
        context['object_list']=Homologacion.objects.filter(refer=self.obj.pk)
        return context

class CategoryListView(ListView):
    model = referencia
    template_name = 'Homologaciones/list2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista homologaciones'
        return context

class Createreferencia(LoginRequiredMixin,SuccessMessageMixin, CreateView):

    # model = referencia
    # fields = [ 'profile','id_dispositivo', 'refer', 'pais', 'name',  'fabricante']
    form_class= ReferenciaForms
#    form_class2= atributo_elemento_hForm
    template_name = 'Homologaciones/new4.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        print(form)
        form.save()
        self.new_refer=form.save()
        messages.success(self.request, 'Form submission successful')
        Homologacion.objects.create(
                refer=referencia.objects.get(pk=self.new_refer.pk),
                profile=self.new_refer.profile,
                tipo=tipo.objects.get(tipo="Oficial")
        )
        return super(Createreferencia, self).form_valid(form)

    def get_success_url(self):
        return reverse('Homologaciones:homologacion', kwargs={ "pk": self.new_refer.pk})
        #return render(request, 'Homologaciones/detail', 1)

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
    form_class= paisForm
    template_name = 'Homologaciones/paises.html'



    def get_context_data(self, **kwargs):
        self.paisFormSet = modelformset_factory(pais, fields=('pais',),extra=pais.objects.all().count())
        context = super(Createpais, self).get_context_data(**kwargs)
        context['formset'] = self.paisFormSet(queryset=pais.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.paisFormSet = modelformset_factory(pais, fields=('pais',),extra=pais.objects.all().count())

        formset = self.paisFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save()
        for instance in instances:
            print("prubeaaaaaa")
            instance.save()
        #return super(Createpais, self).form_valid(form)
        #return HttpResponseRedirect('Homologaciones:home')
        return redirect(self.get_success_url())

    def get_success_url(self):
         return reverse('Homologaciones:home')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['paises'] = queryset=pais.objects.all()
    #     return context
