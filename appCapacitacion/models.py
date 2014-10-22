#encoding: utf-8
from django.db import models

# Create your models here.
class Profesion(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name='Descripción:')
    abreviatura = models.CharField(max_length=10, verbose_name='Abreviatura:')

    def __unicode__(self):
        return self.descripcion

class Dependencia(models.Model):
    nombre_dependencia = models.CharField(max_length=200,verbose_name='Nombre de la dependencia:')
    abreviatura = models.CharField(max_length=10,verbose_name='Abreviatura:')

    def __unicode__(self):
        return self.nombre_dependencia

class TipoEstudio(models.Model):
    nombre_estudio = models.CharField(max_length=50, verbose_name='Tipo de estudio:')


    def __unicode__(self):
        return self.nombre_estudio

class Capacitacion(models.Model):
    TIPO = [
        (1,'Actitud'),
        (2,'Aptitud'),
        (3,'Otros')
    ]

    nombre_capacitacion = models.CharField(max_length=200)
    tipo = models.IntegerField(default=0, choices=TIPO, null=True, blank=True)
    objetivo = models.TextField()
    contenido = models.TextField()
    habilidades = models.TextField()
    impacto = models.TextField()
    horas = models.CharField(max_length=3)
    tipo_estudio = models.ForeignKey(TipoEstudio)

    def __unicode__(self):
        return self.nombre_capacitacion


class Categoria(models.Model):
    ESTATUS = [
        (1,'Vigente'),
        (2,'No vigente')
    ]
    clave = models.CharField(max_length=10)
    nombre_categoria = models.CharField(max_length=100)
    estatus = models.IntegerField(default=0, choices=ESTATUS)

    def __unicode__(self):
        return self.nombre_categoria

class Area(models.Model):
    nombre_area = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre_area



class Instructor(models.Model):
    ESTATUS = [
        (1,'Vigente'),
        (2,'No Vigente')
    ]
    rfc = models.CharField(max_length=14)
    nombre_instructor = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    profesion = models.ForeignKey(Profesion)
    fecha_ingreso = models.DateField(auto_now_add=False)
    estatus = models.IntegerField(default=0, choices=ESTATUS, null=True, blank=True)
    dependencia = models.ForeignKey(Dependencia)
    area = models.ForeignKey(Area)
    categoria = models.ForeignKey(Categoria)
    departamento = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)


    def __unicode__(self):
        return self.rfc

class ServidorPublico(models.Model):
    rfc = models.CharField(max_length=14)
    nombre = models.CharField(max_length=100)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    profesion = models.ForeignKey(Profesion)
    fecha_ingreso = models.DateField(auto_now=False)
    dependencia = models.ForeignKey(Dependencia)
    area = models.ForeignKey(Area)
    departamento = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria)
    puesto = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre