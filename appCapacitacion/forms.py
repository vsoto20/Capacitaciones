#encoding:utf-8
from django.forms import ModelForm
from django import forms
from appCapacitacion.models import *

class ProfesionForm(ModelForm):
    class Meta:
        model = Profesion

class DependenciaForm(ModelForm):
    class Meta:
        model = Dependencia

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor