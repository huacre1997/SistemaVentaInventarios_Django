# Generated by Django 3.0.7 on 2020-08-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturaenc',
            old_name='descuento',
            new_name='igv',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Jurídica', 'Jurídica'), ('Natural', 'Natural')], default='NAT', max_length=10),
        ),
    ]