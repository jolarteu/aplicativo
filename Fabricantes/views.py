from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from Fabricantes.models import fabricante, fabricante_pais
from django.contrib import messages
from django.urls import reverse
from Fabricantes.forms import FabricantesPaisUpdate, FabricantesPaisForm
from django.shortcuts import render, redirect

# Create your views here.
@login_required()
def home(request):

    return render(request, 'Fabricantes/home.html')



class CreateFabricante(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = fabricante
    fields = [ 'fabricante']
    template_name = 'Fabricantes/new.html'

    def form_valid(self, form):
        form.save()
        # form.instance.User = self.request.User
        # print(self.request.User)
        messages.success(self.request, 'Form submission successful')
        return super(CreateFabricante, self).form_valid(form)

    def get_success_url(self):
        return reverse('Homologaciones:home')

class CategoryListView(LoginRequiredMixin, ListView):
    model = fabricante
    template_name = 'Fabricantes/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de fabricantes'
        return context

    def post(self, request):
        self.pk=request.POST['key']
        self.function=request.POST['function']


        return redirect(self.get_success_url(self.pk))

    def get_success_url(self, pk):
        # return reverse('Homologaciones:consultar_terminal/'+pk)
        return reverse('Fabricantes:Create_represtante',kwargs={'pk': pk})           #asi se redirige bien :)


class FabricanteDetailView(LoginRequiredMixin, DetailView):

    model = fabricante_pais
    template_name = 'Fabricantes/lista_por_paises.html'

    queryset = fabricante.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['comparar']=estado.objects.get(pk='En curso')
        context['title'] = 'Lista homologaciones'
        context['object_list']=fabricante_pais.objects.filter(fabricante=self.obj.pk)
        return context

class FabricantePaisUpdate(LoginRequiredMixin, DetailView,UpdateView):

    form_class=FabricantesPaisUpdate
    template_name='Fabricantes/terminar.html'

    queryset = fabricante_pais.objects.all()

    def post(self, request , *args, **kwargs):
        self.obj = super().get_object()

        form=FabricantesPaisUpdate(request.POST, instance=self.obj)
    #    form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)


    def form_valid(self, form):

        form.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
         return reverse('Fabricantes:lista_fabricantes')

class CreateFabricantePais(LoginRequiredMixin, DetailView,  CreateView):
    form_class=FabricantesPaisForm
    model = fabricante_pais
    template_name='Fabricantes/representantes.html'
    queryset = fabricante.objects.all()

    def get_object(self, queryset=None):
        self.obj = super().get_object()
        return self.obj

    def form_valid(self, form):
        f=form.save(commit=False)
        f.fabricante=self.get_object()
        form.save()
        # form.instance.User = self.request.User
        # print(self.request.User)
        messages.success(self.request, 'Form submission successful')
        return redirect(self.get_success_url(f.fabricante))

    def get_success_url(self, pk):
        return reverse('Fabricantes:lista_fabricantes_pais',kwargs={'pk': pk})           #asi se redirige bien :)
