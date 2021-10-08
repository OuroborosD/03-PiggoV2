# Generated by Django 3.2.7 on 2021-10-06 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20211006_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_despesa',
            field=models.DateField(default=datetime.date(2021, 10, 6)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_pagamento',
            field=models.DateField(default=datetime.date(2021, 10, 6)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True),
        ),
    ]
