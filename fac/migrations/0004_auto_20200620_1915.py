# Generated by Django 3.0.7 on 2020-06-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0003_auto_20200618_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(error_messages={'unique': 'Ese nombre ya se encuentra registrado'}, max_length=100, unique=True),
        ),
    ]