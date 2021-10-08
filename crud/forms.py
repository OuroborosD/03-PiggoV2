from django import forms
from django.forms import fields, widgets
from django.forms.forms import Form
from  utils import choices

from .models import Emprestimo, Receita

class DateInput2(forms.DateInput):# para colocar o input precisa criar, o widget.
    input_type = 'date'



class DespesaForm(forms.Form):
    data = forms.DateField(label='data',required=False,widget=DateInput2)
    descricao = forms.CharField(label='descricao',max_length=30,min_length=5)
    meio_pagamento = forms.ChoiceField(label='meio de pagamento', choices = choices.meio_pagamento)
    tipo_despesa = forms.ChoiceField(label='tipo de despesa', choices = choices.tipo_despesa)
    valor  = forms.DecimalField(max_digits=6, decimal_places=2)
    parcelas = forms.IntegerField(min_value=1, initial=1)
    #user_id = forms.IntegerField()

class EmprestimoForm(forms.Form):
    nome = forms.CharField(max_length=30, required=False)
    data_emprestimo = forms.DateField( required=False)
    data_pagamento = forms.DateField()
    descricao = forms.CharField(max_length=50)
    meio_pagametno = forms.ChoiceField(choices=choices.meio_pagamento)
    valor_emprestimo  = forms.DecimalField(max_digits=6, decimal_places=2)
    valor_apagar  = forms.DecimalField(max_digits=6, decimal_places=2)
    parcelas = forms.IntegerField()
    pago = forms.BooleanField()
    #id_autor = forms.IntegerField()

class  ReceitaForm(forms.Form):
    data_receita = forms.DateField(required=False)
    descricao = forms.CharField(max_length=50)
    forma_receita = forms.ChoiceField(choices=choices.fonte_receita)
    valor  = forms.DecimalField(max_digits=6, decimal_places=2)
    recorrencia = forms.BooleanField()
    #id_user = forms.IntegerField()


class EmprestimoModelForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        exclude = ['id_autor']
        labels = {
        
            'data_emprestimo':'data do emprestimo',
            'data_pagamento': 'data do pagamento',
            'descricao':'descrição',
            'meio_pagametno':'meio de pagamento',
            'valor_emprestimo':'valor_emprestimo',
            'valor_apagar':'valor_apagar',
        }
        error_messages = {
            "data_pagamento":{
                'invalid':'data coloca é invalida!'
            },
            "data_emprestimo":{
                'invalid':'data coloca é invalida!'
            }
        }

        widgets = {
            'data_pagamento':forms.DateInput(attrs={'type':'date'}, format='%d/%m/%Y'),
             "data_emprestimo":DateInput2        }

class ReceitaModelForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'
        exclude = ['id_user']
        widgets = {
            'data_receita':DateInput2,
            
        }