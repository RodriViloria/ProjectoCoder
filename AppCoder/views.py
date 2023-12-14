from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()

    return HttpResponse(curso.nombre)


