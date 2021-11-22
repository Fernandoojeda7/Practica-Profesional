from django import forms


from .models import Actividad, Aparato, Clase, Clase_Socio, Entrenador, Entrenador_actividad, Sala, Socio, Socio_actividad

class AparatoForm(forms.ModelForm):

    class Meta:
        model = Aparato
        fields = ['estado', 'descripcion',]
        
class ClaseForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = ['dia', 'horario',]


class EntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador
        fields = ['dni_entrenador', 'nombre_apellido', 'telefono','experiencia','titulo','clase_cd',]


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['descripcion', 'clase_codigo',]


class SalaForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = ['metros_cuadrados', 'ubicacion', 'tipo','aparato_cod','clase_cod',]


class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        fields = ['dni_socio', 'nombre_apellido', 'profesion','telefono','cbu','direccion',]



class Clase_SocioForm(forms.ModelForm):

    class Meta:
        model = Clase_Socio
        fields = ['dni_soc','codgo_clase','descripcion',]



class Entrenador_actividadForm(forms.ModelForm):

    class Meta:
        model = Entrenador_actividad
        fields = ['entrenador_dni', 'activ_id', 'descripcion',]



class Socio_actividadForm(forms.ModelForm):

    class Meta:
        model = Socio_actividad
        fields = ['scio_dni', 'id_activ','descripcion',]




