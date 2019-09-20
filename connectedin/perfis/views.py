from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil
# Create your views here.
# Aqui elaboramos a resposta para o usuario quando ele acessar a aplicacao

#funcao de view
def index(request):
    return render(request,'index.html',{"perfis": Perfil.objects.all()})

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request,"perfil.html",{"perfil" : perfil})