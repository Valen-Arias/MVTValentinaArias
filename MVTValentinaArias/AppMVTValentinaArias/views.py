from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template, Context

from AppMVTValentinaArias.models import Familiar

# Create your views here.


def familiar(request, nombre, apellido, edad, fecha_nacimiento):
    
    familiar = Familiar(nombre = nombre, apellido = apellido, edad = edad, fecha_nacimiento = fecha_nacimiento)
    familiar.save()

    diccionario = {"nombre": nombre, "apellido": apellido, "edad": edad, "fecha_nacimiento": fecha_nacimiento}

    plantilla = loader.get_template("agregar-familiar.html")

    # familiares = Familiar.objects.all

    # return render(request, "agregar-familiar.html", {"familiar": familiares})

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

    # return HttpResponse(documento)

    # lista_familiares = Familiar.objects.all()

    # documento = plantilla.render({lista_familiares})

    # return HttpResponse(documento)