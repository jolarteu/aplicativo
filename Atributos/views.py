from django.shortcuts import render
from django.contrib.auth.decorators import login_required #pide iniciar seccion

# Create your views here.
@login_required()
def home(request):

    return render(request, 'Atributos/home.html')
