# Generated by Django 3.2.7 on 2021-10-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20211004_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_despesa',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='meio_pagametno',
            field=models.CharField(choices=[('0', 'selecione uma opção'), ('1', 'boleto'), ('2', 'dinheiro/debito'), ('3', 'credito')], max_length=30),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.CharField(choices=[('0', 'selecione uma opção'), ('1', 'lanche'), ('2', 'mercado'), ('3', 'compras Online')], max_length=30),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='meio_pagametno',
            field=models.CharField(choices=[('0', 'selecione uma opção'), ('1', 'boleto'), ('2', 'dinheiro/debito'), ('3', 'credito')], max_length=30),
        ),
        migrations.AlterField(
            model_name='receita',
            name='forma_receita',
            field=models.CharField(choices=[('0', 'selecione uma opção'), ('1', 'salario'), ('2', 'mesada'), ('3', 'emprestimo')], max_length=30),
        ),
    ]
