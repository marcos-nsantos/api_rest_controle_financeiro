# Generated by Django 3.2.11 on 2022-01-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Vencimento'),
        ),
    ]