from django.shortcuts import render, redirect
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.forms import modelformset_factory, inlineformset_factory
from django import forms
# from post.models import Post
# from post.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from Homologaciones.models import Homologacion, pais, fabricante, tipo, referencia, estado, resultado, atributo_elemento_h
from Homologaciones.forms import paisForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from Dispositivos.models import dispositivo as dispositivo_id
from Dispositivos.models import dispositivo_atributo
from django.views.generic.edit import FormMixin
from Homologaciones.forms import  HomologacionForm, atributo_elemento_hForm, ReferenciaForms, paisForm, HomologacionUpdateForm
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


class  Homologacion_terminar(DetailView ,UpdateView):
    model=Homologacion
    template_name= 'Homologaciones/terminar.html'
    form_class=HomologacionUpdateForm

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
        self.paisFormSet = modelformset_factory(atributo_elemento_h, fields=('atributo','valor','document'),
        extra=self.cantidad(), widgets={
            'valor': forms.TextInput(attrs={'class': 'myfieldclass'}),
            })


        return self.paisFormSet


    def form_set_2(self, *args, **kwargs):
        self.paisFormSet = modelformset_factory(Homologacion, fields=('__all__'),
        )
        return self.paisFormSet

    def cantidad(self, **kwargs):
        extra=dispositivo_atributo.objects.filter(id_dispositivo=self.obtener_dispositivo()).count()
        return extra

    def lista(self, **kwargs):
        lista=dispositivo_atributo.objects.filter(id_dispositivo=self.obtener_dispositivo())
        lista=[(lista[i].pk, lista[i]) for i in range(len(lista))]
        return lista

    def contexto(self, **kwargs):
        pass
        return self.formset

    def get_context_data(self, **kwargs):
        self.obtener_dispositivo()
        self.HomologacionFormSet = self.form_set_2()
        self.paisFormSet = self.form_set()
        formset2=self.HomologacionFormSet(queryset=Homologacion.objects.none())
        formset=self.paisFormSet(queryset=dispositivo_atributo.objects.none())
        for i in range(self.cantidad()):
            formset[i].fields['atributo'].choices = self.lista()
            formset[i].fields['atributo'].initial  = (self.lista()[i])[0]

        #formset[0].fields['atributo'].choices = [(1,4),(2,2),(3,3)]
    #    formset[0].fields['atributo'].choices = self.lista()
        context = super(Homologacion_terminar, self).get_context_data(**kwargs)
    #    context['formset'] = self.paisFormSet(queryset=dispositivo_atributo.objects.none())
        #context['formset2'] = formset2
        context['formset'] = formset
        context['title'] = 'terminar homologacion'
        #context['pk']=Homologacion.objects.get(pk=self.obj.pk)
        return context

    def post(self, request , *args, **kwargs):
        self.obj = super().get_object()
        self.HomologacionFormSet = self.form_set_2()
        self.paisFormSet = self.form_set()
        formset2 = self.HomologacionFormSet(request.POST)
    #    form1=self.form(request.POST)
        formset = self.paisFormSet(request.POST, request.FILES)
        form=HomologacionUpdateForm(request.POST, request.FILES, instance=self.obj)
    #    form = self.get_form()
        user = Profile.objects.get(pk=request.user.profile.pk)
        if formset.is_valid() and form.is_valid():
            return self.form_valid(formset,form, user)


    def form_valid(self, formset, form, user):

        self.obj = super().get_object()
        instances = formset.save(commit=False)
        f=form.save(commit=False)
        if (f.resultado==resultado.objects.get(pk='Sin terminar')):
            f.estado=estado.objects.get(pk='En curso')
        else:
            f.estado=estado.objects.get(pk='Cerrada')
        f.save()
        # f.profile=user
        # f.refer=referencia.objects.get(pk=sel.obj.refer)
        #instance2= form.save(commit=False)
        for instance in instances:
            instance.Homologacion=Homologacion.objects.get(pk=self.obj.pk)
            #instance.profile=Profile.objects.get(pk=2)          #colocar para detectar usuario IMPORTANTE
            instance.profile=user           #SE PUDO :)
            instance.save()

        #return super(Createpais, self).form_valid(form)
        #return HttpResponseRedirect('Homologaciones:home')
        return redirect(self.get_success_url())

    def get_success_url(self):
         return reverse('Homologaciones:consultar')             #llenar datos para la homologacion

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
        context['comparar']=estado.objects.get(pk='En curso')
        context['title'] = 'Lista homologaciones'
        context['object_list']=Homologacion.objects.filter(refer=self.obj.pk)
        return context          #ver homologaciones de cadad terminal

class detalles_homologacionDetailview(LoginRequiredMixin, DetailView):
    model = atributo_elemento_h
    template_name = 'Homologaciones/detalles_homologacion.html'

    queryset= Homologacion.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Homologacion.objects.filter(pk=self.obj.pk)
        context['object_list']=atributo_elemento_h.objects.filter(Homologacion=self.obj.pk)

        return context          #ver homologaciones de cadad terminal           #lista de atributos

class CategoryListView(LoginRequiredMixin, ListView):
    model = referencia
    template_name = 'Homologaciones/list2.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista homologaciones'

        return context          #lista de terminales


    def get_success_url_1(self, pk):
        # return reverse('Homologaciones:consultar_terminal/'+pk)
        return reverse('Homologaciones:consultar_terminal',kwargs={'pk': pk})           #asi se redirige bien :)

    def get_success_url_3(self, pk):
        # return reverse('Homologaciones:consultar_terminal/'+pk)
        return reverse('Homologaciones:terminar',kwargs={'pk': pk})           #asi se redirige bien :)


    def post(self, request):
        self.pk=request.POST['key']
        self.function=request.POST['function']

        if self.function=="plus":
            Homologacion.objects.create(
                refer=referencia.objects.get(pk=self.pk),
                profile=Profile.objects.get(pk=request.user.profile.pk),
                tipo=tipo.objects.get(tipo="Oficial")

            )
            return redirect(self.get_success_url_1(self.pk))

        elif self.function=="delete":
            referencia.objects.filter(pk=self.pk).delete()
            return redirect(self.get_success_url_2())

        elif self.function=="see":
            Homologacion_t=Homologacion.objects.filter(refer=self.pk).last().pk
            return redirect(self.get_success_url_3(Homologacion_t))


    def get_success_url_2(self):
         return reverse('Homologaciones:consultar')


    # def form_valid(self, form):
    #     self.pk = self.request.pk
    #     messages.success(self.request, 'Form submission successful')
    #     Homologacion.objects.create(
    #               refer=referencia.objects.get(pk=32),
    #               profile=Profile.objects.get(pk=request.user.profile.pk),
    #               tipo=tipo.objects.get(tipo="Oficial")
    #     )
    #     return redirect(self.get_success_url())


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
        return reverse('Homologaciones:consultar_terminal', kwargs={ "pk": self.new_refer.pk})
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
