from django.contrib import admin

# Register your models here.
from .models import Receita,Despesa,Emprestimo


admin.site.register(Receita)

admin.site.register(Despesa)

admin.site.register(Emprestimo)