# Generated by Django 3.2.11 on 2022-01-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_remove_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Health', 'Health'), ('Home', 'Home'), ('Transport', 'Transport'), ('Education', 'Education'), ('Leisure', 'Leisure'), ('Unforeseen', 'Unforeseen'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
