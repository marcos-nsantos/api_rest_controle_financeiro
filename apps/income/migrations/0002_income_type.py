# Generated by Django 3.2.11 on 2022-01-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.IntegerField(choices=[(1, 'Fixed'), (2, 'Variable')], default=1),
            preserve_default=False,
        ),
    ]
