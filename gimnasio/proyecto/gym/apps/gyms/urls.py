from apps.gyms.views import *
from django.urls import *

urlpatterns= [

    path('aparato_form/', crearAparato, name='crear Aparato' ), 
    path('', inicio, name='index' ),
    path('clase_form/', crearClase, name= 'crear Clase' ),
    path('entrenador_form/', crearEntrenador, name= 'crear Entremador' ),
    path('actividad_form/', crearActividad, name= 'crear Actividad' ),
    path('sala_form/', crearSala, name= 'crear Sala' ),
    path('socio_form/', crearSocio, name= 'crear Socio' ),
    path('clase_socio_form/', crearClase_Socio, name= 'crear Clase-Socio' ),
    path('entrenador_actividad_form/', crearEntrenador_actividad, name= 'crear Entrenador-Actividad' ),
    path('socio_actividad_form/', crearSocio_actividad, name= 'crear Socio-Actividad' ),
    

]