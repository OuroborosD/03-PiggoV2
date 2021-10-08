from django.shortcuts import render
from django.shortcuts  import render, redirect
from django.contrib.auth.models import UserManager
from django.contrib import auth


#   feitos aqui.
from .forms import Create, Login
from .models import CustomUser

def create(request):
    if request.method == 'POST':
        dados_cadastro = Create(request.POST)
        print(dados_cadastro['usuario'])
        if dados_cadastro.is_valid():
            nome = dados_cadastro.cleaned_data['nome']
            usuario = dados_cadastro.cleaned_data['usuario']
            senha = dados_cadastro.cleaned_data['senha']
            email = dados_cadastro.cleaned_data['email']
            cartao = dados_cadastro.cleaned_data['cartao']

            if CustomUser.objects.filter(username=usuario).exists() and  CustomUser.objects.filter(email=email).exists() :
                print('usuario já existe')
               
            else:

                if cartao is None:
                    CustomUser.objects.create_user(username=usuario,
                                                    first_name = nome,
                                                    password=senha,
                                                    email=email)
                else:   
                    CustomUser.objects.create_user(username=usuario,
                                                    first_name = nome,
                                                    password=senha,
                                                    email=email,
                                                    vencimento_cartao=cartao)
                return redirect('accounts_login')
                
        else:
            print('não validos')

    else: 
        dados_cadastro = Create()

    context = {
        'forms':dados_cadastro
    }
    
    return render(request,'accounts/cadastro.html',context)


def login(request):

    if request.method == 'POST':

        dados_login = Login(request.POST)
        if dados_login.is_valid():
            usuario = dados_login.cleaned_data['usuario']
            senha = dados_login.cleaned_data['senha']
            user = auth.authenticate(request, username=usuario,password=senha)

            if user: # se o user der certo, ele é True
                auth.login(request,user)
                return redirect('accounts_dashboard')
            else:
                print('usuario invalido!!')

    
    else:

        dados_login = Login()
    
    context = {
        'forms': dados_login
    }

    return render(request,'accounts/login.html',context)


def dashboard(request):
    return render(request,'accounts/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts_login')