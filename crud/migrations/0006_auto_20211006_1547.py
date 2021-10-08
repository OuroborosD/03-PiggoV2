# Generated by Django 3.2.7 on 2021-10-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_despesa_data_despesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='meio_pagametno',
            field=models.CharField(choices=[(None, 'selecione uma opção'), ('1', 'boleto'), ('2', 'dinheiro/debito'), ('3', 'credito')], max_length=30),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.CharField(choices=[(None, 'selecione uma opção'), ('1', 'lanche'), ('2', 'mercado'), ('3', 'compras Online')], max_length=30),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='meio_pagametno',
            field=models.CharField(choices=[(None, 'selecione uma opção'), ('1', 'boleto'), ('2', 'dinheiro/debito'), ('3', 'credito')], max_length=30),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='forma_receita',
            field=models.CharField(choices=[(None, 'selecione uma opção'), ('1', 'salario'), ('2', 'mesada'), ('3', 'emprestimo')], max_length=30),
        ),
    ]