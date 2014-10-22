#encoding: utf-8
from django.shortcuts import render,render_to_response, HttpResponseRedirect, get_object_or_404
from django.template import RequestContext
from appCapacitacion.models import *
from appCapacitacion.forms import *
from django.contrib import messages
# Create your views here.
def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))

def nueva_profesion(request):
    if request.method == 'POST':
        formulario = ProfesionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje="Se ha registrado correctamente una profesión."
            messages.success(request,mensaje)
            return HttpResponseRedirect('/profesion/nueva')
    else:
            formulario = ProfesionForm()
    return render_to_response('profesionform.html',{'formulario':formulario}, context_instance=RequestContext(request))


def nueva_dependencia(request):
    if request.method == 'POST':
        formulario = DependenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/dependencia/nueva')
    else:
        formulario=DependenciaForm()
    return render_to_response('dependenciaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def lista_profesion(request):
    profesion = Profesion.objects.all()
    return render_to_response('lista_profesiones.html',{'profesiones':profesion},\
		context_instance=RequestContext(request))

def lista_dependencia(request):
    dependencia = Dependencia.objects.all()
    return render_to_response('lista_dependencias.html',{'dependencias':dependencia},\
		context_instance=RequestContext(request))

def profesion_eliminar(request,profesion_id):
    profesion = Profesion.objects.get(pk=profesion_id)
    profesion.delete()
    return HttpResponseRedirect('/profesion/consultar')

def dependencia_eliminar(request,dependencia_id):
    dependencia = Dependencia.objects.get(pk=dependencia_id)
    dependencia.delete()
    return HttpResponseRedirect('/dependencia/consultar')

def profesion_editar(request,profesion_id):
    profesion = get_object_or_404(Profesion, pk=profesion_id)
    if request.method == 'POST':
        formulario = ProfesionForm(request.POST, instance=profesion)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/profesion/consultar')
    else:
        formulario = ProfesionForm(instance=profesion)
    return render_to_response('profesion_editar.html', {'formulario': formulario}, context_instance=RequestContext(request))

def dependencia_editar(request,dependencia_id):
    dependencia= get_object_or_404(Dependencia, pk=dependencia_id)
    if request.method == 'POST':
        formulario = DependenciaForm(request.POST, instance=dependencia)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/dependencia/consultar')
    else:
        formulario = DependenciaForm(instance=dependencia)
    return render_to_response('dependencia_editar.html', {'formulario':formulario}, context_instance=RequestContext(request))


def nuevo_instructor(request):
    if request.method == 'POST':
        formulario = InstructorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje="Se ha registrado correctamente una profesión."
            messages.success(request,mensaje)
            return HttpResponseRedirect('/instructor/nuevo')
    else:
            formulario = InstructorForm()
    return render_to_response('instructorform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def lista_instructor(request):
    instructor = Instructor.objects.all()
    return render_to_response('lista_instructor.html',{'instructores':instructor},\
		context_instance=RequestContext(request))


