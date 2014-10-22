from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Capacitaciones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','appCapacitacion.views.inicio'),
    url(r'^profesion/nueva/$','appCapacitacion.views.nueva_profesion'),
    url(r'^profesion/consultar/$','appCapacitacion.views.lista_profesion'),
    url(r'^profesion/eliminar/(?P<profesion_id>\d+)/$','appCapacitacion.views.profesion_eliminar'),
    url(r'^profesion/editar/(?P<profesion_id>\d+)/$','appCapacitacion.views.profesion_editar'),

    url(r'^dependencia/nueva/$','appCapacitacion.views.nueva_dependencia'),
    url(r'^dependencia/eliminar/(?P<dependencia_id>\d+)/$','appCapacitacion.views.dependencia_eliminar'),
    url(r'^dependencia/consultar/$','appCapacitacion.views.lista_dependencia'),
    url(r'^dependencia/editar/(?P<dependencia_id>\d+)/$', 'appCapacitacion.views.dependencia_editar'),

    url(r'^instructor/nuevo/$','appCapacitacion.views.nuevo_instructor'),
    url(r'^instructor/consultar/$','appCapacitacion.views.lista_instructor'),


)
