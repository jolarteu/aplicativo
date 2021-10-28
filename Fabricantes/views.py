from django.shortcuts import render
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from Fabricantes.models import fabricante
from django.contrib import messages
from django.urls import reverse

# Create your views here.
@login_required()
def home(request):

    return render(request, 'Fabricantes/home.html')



class CreateFabricante(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = fabricante
    fields = [ 'fabricante']
    template_name = 'Fabricantes/new.html'

    def form_valid(self, form):
        print("holiiiiiiiii")
        # form.instance.User = self.request.User
        # print(self.request.User)
        form.save()
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
