from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppMVTValentinaArias.models import Familiar

# Create your views here.


def familiar(request, nombre, apellido, edad, fecha_nacimiento):
    
    familiar = Familiar(nombre = nombre, apellido = apellido, edad = edad, fecha_nacimiento = fecha_nacimiento)
    familiar.save()

    diccionario = {"nombre": nombre, "apellido": apellido, "edad": edad, "fecha_nacimiento": fecha_nacimiento}

    plantilla = loader.get_template("agregar-familiar.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)



def lista_familiares(request):

    lista = Familiar.objects.all()

    return render(request, "mostrar-familiares.html", {"lista_familiares": lista})