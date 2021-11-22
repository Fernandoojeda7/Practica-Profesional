from django.db import models
from django.db.models.base import Model
# Create your models here.

class Aparato(models.Model):
    id_aparato= models.AutoField(primary_key=True)
    estado= models.CharField(max_length=200, blank=False, null=False)
    descripcion= models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Aparato'
        verbose_name_plural = 'Aparatos'
        ordering = ['estado']

    def __str__(self):
        return self.estado

class Clase(models.Model):
    cod_clase= models.AutoField(primary_key=True)
    dia= models.CharField(max_length=200, blank=False, null=False)
    horario= models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name= 'Clase'
        verbose_name_plural = 'Clases'
        ordering = ['dia']

    def __str__(self):
        return self.dia

class Entrenador(models.Model):
    dni_entrenador= models.CharField(primary_key=True, max_length=20)
    nombre_apellido= models.CharField(max_length=200, blank=False, null=False)
    telefono= models.CharField(max_length=20, blank=False, null=False)
    experiencia= models.CharField(max_length=200, blank=False, null=False)
    titulo= models.CharField(max_length=200, blank=False, null=False)
    clase_cd= models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Entrenador'
        verbose_name_plural = 'Entrenadores'
        ordering = ['nombre_apellido']

    def __str__(self):
        return self.nombre_apellido

class Actividad(models.Model):
    id_actividad= models.AutoField(primary_key=True)
    descripcion= models.TextField(blank=False, null=False)
    clase_codigo= models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion

class Sala(models.Model):
    id_sala= models.AutoField(primary_key=True)
    metros_cuadrados= models.CharField(max_length=20, blank=False, null=False)
    ubicacion= models.CharField(max_length=200, blank=False, null=False)
    tipo= models.CharField(max_length=200, blank=False, null=False)
    aparato_cod= models.ForeignKey(Aparato, on_delete=models.CASCADE)
    clase_cod= models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['metros_cuadrados']

    def __str__(self):
        return self.metros_cuadrados

class Socio(models.Model):
    dni_socio= models.CharField(primary_key=True, max_length=20)
    nombre_apellido= models.CharField(max_length=200, blank=False, null=False)
    profesion= models.CharField(max_length=200, blank=False, null=False)
    telefono= models.CharField(max_length=20, blank=False, null=False)
    cbu= models.CharField(max_length=20, blank=False, null=False)
    direccion= models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name= 'Socio'
        verbose_name_plural = 'Socios'
        ordering = ['nombre_apellido']

    def __str__(self):
        return self.nombre_apellido

class Clase_Socio(models.Model):
    dni_soc= models.ForeignKey(Socio, on_delete=models.CASCADE)
    codgo_clase= models.ForeignKey(Clase, on_delete=models.CASCADE)
    descripcion= models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Clase-Socio'
        verbose_name_plural = 'Clases-Socios'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion 

class Entrenador_actividad(models.Model):
    entrenador_dni=  models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    activ_id= models.ForeignKey(Actividad, on_delete=models.CASCADE)
    descripcion= models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Entrenador-Actividad'
        verbose_name_plural = 'Entrenadores-Actividades'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion 

class Socio_actividad(models.Model):
    scio_dni= models.ForeignKey(Socio, on_delete=models.CASCADE)
    id_activ= models.ForeignKey(Actividad, on_delete=models.CASCADE)
    descripcion= models.TextField(blank=False, null=False)

    class Meta:
        verbose_name= 'Socio-Actividad'
        verbose_name_plural = 'Socios-Actividades'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion 