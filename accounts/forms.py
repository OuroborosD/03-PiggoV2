from django import forms
from django.forms.forms import Form


class CreateForms(forms.Form):
    usuario = forms.CharField(label='usuario: ',
                              min_length=5,
                              max_length=20, 
                              widget=forms.TextInput(attrs={'placeholder': 'Seu usuario aqui'}))#adiciona um placeholder
    senha = forms.CharField(label='senha: ',
                            min_length=1, 
                            max_length=12, 
                            widget=forms.TextInput(attrs={'placeholder': 'senha aqui'}))

class  LoginForms(forms.Form):
    usuario = forms.CharField(label='usuario: ',
                              min_length=5,
                              max_length=20, 
                              widget=forms.TextInput(attrs={'placeholder': 'Seu usuario aqui'}))#adiciona um placeholder
    senha = forms.CharField(label='senha: ',
                            min_length=1, 
                            max_length=12, 
                            widget=forms.TextInput(attrs={'placeholder': 'senha aqui'}))