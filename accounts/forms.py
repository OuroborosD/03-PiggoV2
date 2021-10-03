from django import forms


class Create(forms.Form):
    nome =   forms.CharField(label='nome', min_length=2)
    usuario   =   forms.CharField(label='usuario', min_length=1)
    email   =   forms.EmailField(label='email', required=False)
    senha   =   forms.CharField(label='senha', min_length=1)
    cartao  =   forms.IntegerField(label='data em que a fatura fecha', required=False)

class Login(forms.Form):
    usuario =   forms.CharField(label='usuario', min_length=2)
    senha   =   forms.CharField(label='usuario', min_length=1)
