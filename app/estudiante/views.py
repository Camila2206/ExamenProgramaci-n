from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .forms import FormularioEstudiante
from app.modelo.models import Estudiante



def principal(request):
    usuario=request.user
    listaEstudiantes= Estudiante.objects.all().filter(estado=True).order_by('apellidos')
    context={
        'lista':listaEstudiantes
    }
    return render(request, 'estudiante/principal.html', context)

def crear(request):
    formulario=FormularioEstudiante(request.POST)
    if request.method=='POST':
        if formulario.is_valid():
            datos=formulario.cleaned_data
            estudiante=Estudiante()
            estudiante.cedula=datos.get('cedula')
            estudiante.numero=datos.get('numero')
            estudiante.carrera=datos.get('carrera')
            estudiante.nombres=datos.get('nombres')
            estudiante.apellidos=datos.get('apellidos')
            estudiante.edad=datos.get('edad')
            estudiante.genero=datos.get('genero')
            estudiante.save()
            return redirect(principal)
    context={
        'f':formulario,
        'mensaje':'Bienvenidos',
    }
    return render(request,'estudiante/crear_estudiante.html', context)


def modificar(request):
    dni=request.GET['cedula']
    estudiante=Estudiante.objects.get(cedula=dni)
    if request.method=='POST':
        formulario=FormularioEstudiante(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            estudiante.cedula=datos.get('cedula')
            estudiante.numero=datos.get('numero')
            estudiante.carrera=datos.get('carrera')
            estudiante.nombres=datos.get('nombres')
            estudiante.apellidos=datos.get('apellidos')
            estudiante.edad=datos.get('edad')
            estudiante.genero=datos.get('genero')
            estudiante.save()
            return redirect(principal)
    else:
        formulario=FormularioEstudiante(instance=estudiante)
        context={
            'f':formulario,
            'mensaje':'Bienvenidos'
        }
        return render(request, 'estudiante/crear_estudiante.html', context)

def eliminar(request):
    dni=request.GET['cedula']
    estudiante=Estudiante.objects.get(cedula=dni)
    estudiante.estado=False
    estudiante.save()
    return redirect(principal)


