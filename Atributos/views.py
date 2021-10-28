from django.shortcuts import render
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.urls import reverse

from Atributos.models import atributo
# Create your views here.
@login_required()
def home(request):

    return render(request, 'Atributos/home.html')



class CreateCaracteristica(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = atributo
    fields = [ 'profile', 'name', 'descripcion']
    template_name = 'Atributos/new.html'

    def form_valid(self, form):

        # form.instance.User = self.request.User
        # print(self.request.User)
        form.save()
        messages.success(self.request, 'Form submission successful')
        return super(CreateCaracteristica, self).form_valid(form)

    def get_success_url(self):
        return reverse('Homologaciones:home')

class CategoryListView(LoginRequiredMixin, ListView):
    model = atributo
    template_name = 'Atributos/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de caracteristicas'
        return context
