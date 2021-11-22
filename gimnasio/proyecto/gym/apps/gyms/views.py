from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.gyms.forms import ActividadForm, AparatoForm, Clase_SocioForm, ClaseForm, Entrenador_actividadForm, EntrenadorForm, SalaForm, Socio_actividadForm, SocioForm




def inicio(request):
    return render(request,'index.html')


def crearAparato(request):
    if request.method == 'POST':  
        aparato = AparatoForm(request.POST)
        if aparato.is_valid(): 
            aparato.save()
            return HttpResponseRedirect('/gyms') 

    else:
        aparato = AparatoForm()

    return render(request, 'gym/aparato_form.html', {'form':aparato})

def crearClase(request):
    if request.method == 'POST':  
        clases = ClaseForm(request.POST)
        if clases.is_valid(): 
            clases.save()
        return HttpResponseRedirect('/gyms') 

    else:
        clases = ClaseForm()

    return render(request, 'gym/clase_form.html', {'form':clases})

def crearEntrenador(request):
    if request.method == 'POST':  
        entrenador = EntrenadorForm(request.POST)
        if entrenador.is_valid(): 
            entrenador.save()
            return HttpResponseRedirect('/gyms') 

    else:
        entrenador = EntrenadorForm()

    return render(request, 'gym/entrenador_form.html', {'form':entrenador})

def crearActividad(request):
    if request.method == 'POST':  
        actividad = ActividadForm(request.POST)
        if actividad.is_valid(): 
            actividad.save()
        return HttpResponseRedirect('/gyms') 

    else:
        actividad = ActividadForm()

    return render(request, 'gym/actividad_form.html', {'form':actividad})

def crearSala(request):
    if request.method == 'POST':  
        sala = SalaForm(request.POST)
        if sala.is_valid(): 
            sala.save()
        return HttpResponseRedirect('/gyms') 

    else:
        sala = SalaForm()

    return render(request, 'gym/sala_form.html', {'form':sala})


def crearSocio(request):
    if request.method == 'POST':  
        socio = SocioForm(request.POST)
        if socio.is_valid(): 
            socio.save()
            return HttpResponseRedirect('/gyms') 

    else:
        socio = SocioForm()

    return render(request, 'gym/socio_form.html', {'form':socio})

def crearClase_Socio(request):
    if request.method == 'POST':  
        claseSocio = Clase_SocioForm(request.POST)
        if claseSocio.is_valid(): 
            claseSocio.save()
        return HttpResponseRedirect('/gyms') 

    else:
        claseSocio = Clase_SocioForm()

    return render(request, 'gym/clase_socio_form.html', {'form':claseSocio})

def crearEntrenador_actividad(request):
    if request.method == 'POST':  
        entrenador_actividad = Entrenador_actividadForm(request.POST)
        if entrenador_actividad.is_valid(): 
            entrenador_actividad()
        return HttpResponseRedirect('/gyms') 

    else:
        entrenador_actividad = Entrenador_actividadForm()

    return render(request, 'gym/entrenador_actividad_form.html', {'form':entrenador_actividad})


def crearSocio_actividad(request):
    if request.method == 'POST':  
        socioactividad = Socio_actividadForm(request.POST)
        if socioactividad.is_valid(): 
            socioactividad.save()
        return HttpResponseRedirect('/gyms') 

    else:
        socioactividad = Socio_actividadForm()

    return render(request, 'gym/socio_actividad_form.html', {'form':socioactividad})