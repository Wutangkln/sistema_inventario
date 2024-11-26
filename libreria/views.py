from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroBusquedaForm

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def libros(request):
    form = LibroBusquedaForm(request.GET)
    libros = Libro.objects.all()

    if form.is_valid():
        busqueda = form.cleaned_data['busqueda']
        if busqueda:
            libros = libros.filter(titulo__icontains=busqueda)
    return render(request, 'index.html', {'libros': libros, 'form':form})





