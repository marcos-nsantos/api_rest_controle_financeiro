# Generated by Django 3.2.11 on 2022-01-24 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='type',
        ),
    ]
