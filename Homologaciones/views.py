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
from Users.models import Profile
from django.contrib.auth.models import User


@login_required()
def home(request):
    return render(request, 'Homologaciones/home.html')

@login_required()
def homologaciones(request):

    return render(request, 'Homologaciones/homologaciones.html')


class  Homologacion_terminar(DetailView, CreateView):
    model=Homologacion
    template_name= 'Homologaciones/terminar.html'
    form_class=atributo_elemento_hForm

    queryset = Homologacion.objects.all()

    # def get_queryset(self):
    #         #self.user = User.objects.filter(profile=self.request.user)
    #         self.user= self.request.user
    #         return self.user

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def obtener_dispositivo(self, *args, **kwargs):
        self.obj=self.get_object()
        self.refer=referencia.objects.get(pk=self.obj.refer.pk)
        self.dispositivo=dispositivo_id.objects.get(pk=self.refer.id_dispositivo.pk)
        return self.dispositivo

    def form_set(self, *args, **kwargs):
        choice=[1, 2]
        self.paisFormSet = modelformset_factory(atributo_elemento_h, fields=('atributo','valor','document'),
        extra=dispositivo_atributo.objects.filter(id_dispositivo=self.obtener_dispositivo()).count())

        # for form in self.paisFormSet(queryset=pais.objects.none()):
        #     form.fields['atributo'].choices=choice

        # #     #i.fields['atributo'].choices=choice
        for i in range (dispositivo_atributo.objects.filter(id_dispositivo=self.obtener_dispositivo()).count()):
            (self.paisFormSet(queryset=pais.objects.none()))[i].fields['atributo'].choices=[]

        return self.paisFormSet

    def get_context_data(self, **kwargs):
        self.obtener_dispositivo()
        self.paisFormSet = self.form_set()
        context = super(Homologacion_terminar, self).get_context_data(**kwargs)
        context['formset'] = self.paisFormSet(queryset=pais.objects.none())
        context['title'] = 'terminar homologacion'
        #context['pk']=Homologacion.objects.get(pk=self.obj.pk)
        return context

    def post(self, request, *args, **kwargs):
        self.paisFormSet = self.form_set()
        formset = self.paisFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        self.obj = super().get_object()
        instances = formset.save(commit=False)
        for instance in instances:
            instance.Homologacion=Homologacion.objects.get(pk=self.obj.pk)
            instance.profile=Profile.objects.get(pk=2)          ##colocar para detectar usuario IMPORTANTE
            instance.save()
        #return super(Createpais, self).form_valid(form)
        #return HttpResponseRedirect('Homologaciones:home')
        return redirect(self.get_success_url())

    def get_success_url(self):
         return reverse('Homologaciones:home')


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

class HomologacionListView(LoginRequiredMixin, DetailView):
    model = Homologacion
    template_name = 'Homologaciones/lista_homologaciones.html'

    queryset = referencia.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista homologaciones'
        context['object_list']=Homologacion.objects.filter(refer=self.obj.pk)
        return context

class CategoryListView(LoginRequiredMixin, ListView):
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
        return reverse('Homologaciones:detail', kwargs={ "pk": self.new_refer.pk})
        #return render(request, 'Homologaciones/detail', 1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fabricantes'] = queryset=fabricante.objects.all()
        context['dispositivos'] = queryset=dispositivo_id.objects.all()
        return context

class Createpais(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = pais
    form_class= paisForm
    template_name = 'Homologaciones/paises.html'



    def get_context_data(self, **kwargs):
        self.paisFormSet = modelformset_factory(atributo_elemento_h, fields='__all__',extra=2)
        context = super(Createpais, self).get_context_data(**kwargs)
        context['formset'] = self.paisFormSet(queryset=pais.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.paisFormSet = modelformset_factory(atributo_elemento_h, fields='__all__',extra=2)
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
