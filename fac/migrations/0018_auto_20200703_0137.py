# Generated by Django 3.0.7 on 2020-07-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0017_auto_20200703_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Jurídica', 'Jurídica'), ('Natural', 'Natural')], default='Natural', max_length=10),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
