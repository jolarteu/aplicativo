from django.shortcuts import render
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from Dispositivos.models import dispositivo
from django.contrib import messages
from django.urls import reverse

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
