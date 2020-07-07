# Generated by Django 3.0.7 on 2020-07-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0012_auto_20200629_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Jurídica', 'Jurídica'), ('Natural', 'Natural')], default='Natural', max_length=10),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
