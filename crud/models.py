
from django.db import models
from django.db.models.deletion import CASCADE
from utils.functions import today_date

# Create your models here.
from utils import choices
from accounts.models import CustomUser

class Despesa(models.Model):
    data_despesa = models.DateField(default=today_date())
    descricao = models.CharField(max_length=50)
    meio_pagametno = models.CharField(max_length=30,choices=choices.meio_pagamento)
    tipo_despesa = models.CharField(max_length=30, choices=choices.tipo_despesa)
    valor  = models.DecimalField(max_digits=6, decimal_places=2)
    parcelas = models.SmallIntegerField(default=1)
    user_id = models.ForeignKey(CustomUser,on_delete=CASCADE, db_column='user_id', default=0)

    def __str__(self):
        return (f'No dia {self.data_despesa}  ouve a compra de um  {self.descricao}      R$:{self.valor}')


class Receita(models.Model):
    data_receita = models.DateField(default=today_date())
    descricao = models.CharField(max_length=50)
    forma_receita = models.CharField(choices=choices.fonte_receita, max_length=30)
    valor  = models.DecimalField(max_digits=6, decimal_places=2)
    recorrencia = models.BooleanField(default=False)
    id_user = models.ForeignKey(CustomUser,on_delete=CASCADE, blank=True,null=True)


    def __str__(self):
        return (f'{self.descricao}  - {self.forma_receita} R$:{self.valor}')

class Emprestimo(models.Model):
    nome = models.CharField(max_length=30)
    data_emprestimo = models.DateField(default=today_date())
    data_pagamento = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=50)
    meio_pagametno = models.CharField(max_length=30,choices=choices.meio_pagamento)
    valor_emprestimo  = models.DecimalField(max_digits=6, decimal_places=2)
    valor_apagar  = models.DecimalField(max_digits=6, decimal_places=2)
    parcelas = models.SmallIntegerField(default=1)
    pago = models.BooleanField(default=False)
    id_autor = models.ForeignKey(CustomUser,on_delete=CASCADE)


    def __str__(self):
        return (f'{self.nome}  - {self.data_emprestimo}  pagar em {self.data_pagamento} o valor R$:{self.valor}')


