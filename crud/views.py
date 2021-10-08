from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required


# self made
from .models import Despesa,Receita,Emprestimo
from .forms import DespesaForm,ReceitaForm, EmprestimoModelForm, ReceitaModelForm

#self made functions
from utils.functions import logged_user
# Create your views here.


class ReceitaView(View):
    def get(self, request):
       form = ReceitaModelForm()
       context = {
           'forms':form
       }
       return render(request,'crud/receita.html', context)
    def post(self,request):
        form = ReceitaModelForm(request.POST)
        if form.is_valid():
            form_with_id = form.save(commit=False) #o commite false, impede que salve no db, mas cria toda a estrutura
            form_with_id.id_user = request.user# pega o usuario atual
            form_with_id.save()# salva no banoco de dados
            print(form.cleaned_data, request.user)
            context = {
           'forms':form
                }
            return render(request,'crud/receita.html', context)
           
    
        
        

@login_required(redirect_field_name='accounts_login')
def despesa(request):
    if request.method == 'POST':
        despesa_dados = DespesaForm(request.POST)
        if despesa_dados.is_valid():
          
            data = despesa_dados.cleaned_data['data']
            descricao = despesa_dados.cleaned_data['descricao']
            meio_pagamento = despesa_dados.cleaned_data['meio_pagamento']
            tipo_despesa = despesa_dados.cleaned_data['tipo_despesa']
            valor = despesa_dados.cleaned_data['valor']
            parcelas = despesa_dados.cleaned_data['parcelas']
            
            user = request.user # necessario passar esse valor para conseguir usaver o usuario na views
            if data != None:
                     Despesa.objects.create(data_despesa=data,
                                            descricao=descricao,
                                            meiomeio_pagametno_pagamento=meio_pagamento,
                                            tipo_despesa=tipo_despesa,
                                            valor=valor,
                                            parcelas=parcelas,
                                            user_id=user
                     )
            else:
                    Despesa.objects.create(
                                            descricao=descricao,
                                            meio_pagametno=meio_pagamento,
                                            tipo_despesa=tipo_despesa,
                                            valor=valor,
                                            parcelas=parcelas,
                                            user_id=user
                     )
            print('salvo com sucesso')
                     
        else:
             print('valores não são validados')

    else:
        despesa_dados = DespesaForm()
    
    context ={
        'forms':despesa_dados
    }
    
    return render(request,'crud/despesa.html',context)

@login_required(redirect_field_name='accounts_login')
def emprestimo(request):
    if request.method == 'POST':
        emprestimo_dados = EmprestimoModelForm(request.POST)
        if emprestimo_dados.is_valid():
            emprestimo_with_id = emprestimo_dados.save(commit=False)
            emprestimo_with_id.id_autor = logged_user(request)
            emprestimo_with_id.save()
            return redirect('accounts_dashboard')

        else:
            print('não validos')
    
    else:
        emprestimo_dados = EmprestimoModelForm()
    
    context ={
        'forms' : emprestimo_dados
    }
    return render(request,'crud/emprestimo.html',context)




if  request.user.is_anonymous:
    #logica