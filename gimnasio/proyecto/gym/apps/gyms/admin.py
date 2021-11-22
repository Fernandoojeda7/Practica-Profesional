from django.contrib import admin


# Register your models here.

from .models import Aparato, Clase, Entrenador, Actividad, Sala, Socio, Clase_Socio, Entrenador_actividad, Socio_actividad

admin.site.register(Aparato)
admin.site.register(Clase)
admin.site.register(Entrenador)
admin.site.register(Actividad)
admin.site.register(Sala)
admin.site.register(Socio)
admin.site.register(Clase_Socio)
admin.site.register(Entrenador_actividad)
admin.site.register(Socio_actividad)
