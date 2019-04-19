from django.shortcuts import render
#from django.http import HttpResponse
from connectedin.perfis.models import Perfil

#def index(request):
    #return HttpResponse('Bem vindo')


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):

    perfil = Perfil()
    if perfil_id == '1':
        perfil = Perfil('Gerson', 'gerson@email.com', '997370753', 'Pathfind')
    return render(request, 'perfil.html')

