from django.shortcuts import render

from .forms import DespesaForm,ReceitaForm,EmprestimoForm
# Create your views here.

def despesa(request):
    if request.method == 'POST':
        despesa_dados = DespesaForm(request.POST)
        print(despesa_dados)
        #if despesa_dados.is_valid():

    else:
        despesa_dados = DespesaForm()
    
    context ={
        'forms':despesa_dados
    }
    
    return render(request,'crud/despesa.html',context)


def receita(request):
    pass

def emprestimo(request):
    pass