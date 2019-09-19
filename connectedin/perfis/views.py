from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Aqui elaboramos a resposta para o usuario quando ele acessar a aplicacao

#funcao de view
def index(request):
    return render(request,'index.html')

def exibir(request,perfil_id):
    return render(request,"perfil.html")