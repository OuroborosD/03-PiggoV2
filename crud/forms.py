from django import forms
from django.forms.forms import Form
from  ultils import choices



class DespesaForm(forms.Form):
    data = forms.DateTimeInput(label='data',required=False)
    descricao = forms.CharField(label='descricao',max_length=30,min_length=5)
    meio_pagamento = forms.ChoiceField(label='meio de pagamento', choices = choices.meio_pagamento)
    tipo_despesa = forms.ChoiceField(label='tipo de despesa', choices = choices.tipo_despesa)
    valor  = forms.DecimalField(max_digits=6, decimal_places=2)
    parcelas = forms.IntegerField(min_value=1, required=False)
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