from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def index(request):
    return HttpResponse('Bem vindo')
=======

def index(request):
    return render(request, 'index.html')


def exibir(request):
    return render(request, 'perfil.html')
>>>>>>> e83b480f9fd311d2a0e6c60992b9fb0e0c0b244c
