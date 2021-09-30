from django import contrib
from accounts import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,UserManager
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import CreateForms, LoginForms

# Create your views here.



def create(request):
    erro = None
    if request.method == 'POST':
        dados = CreateForms(request.POST) #pega todos os dados do formulario

        if dados.is_valid():
            usuario =  dados.cleaned_data['usuario']
            senha = dados.cleaned_data['senha']
            print(usuario,'==============', senha)
            if User.objects.filter(username=usuario).exists():
                print('username já existe.')
                erro = 1
            else:# se chegou até aqui é que está tudo correto e pode salvar
                User.objects.create_user(username=usuario,password=senha)
                return redirect('accounts_login')

    dados = CreateForms()#vai para o banco de dados
    
    context ={
        'forms':dados,
        'erros':erro
    }

    return render(request,'accounts/create.html', context)

def login(request):
    
    if request.method == 'POST':
        user = LoginForms(request.POST)
        
        if user.is_valid():
            usuario = user.cleaned_data['usuario']
            senha = user.cleaned_data['senha']

            user = auth.authenticate(request, username=usuario, password=senha)
            if user:
                print('entrou no login')
                auth.login(request,user)
                return redirect('accounts_dashboard')
            else:
                  print('=========não entrou no login')
    user = LoginForms()

    context ={
        'form':user
    }

    return render(request,'accounts/login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('accounts_login')

@login_required(redirect_field_name='accounts_login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')