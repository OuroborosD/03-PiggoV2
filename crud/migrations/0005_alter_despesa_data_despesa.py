# Generated by Django 3.2.7 on 2021-10-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20211004_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_despesa',
            field=models.DateField(auto_now=True),
        ),
    ]
