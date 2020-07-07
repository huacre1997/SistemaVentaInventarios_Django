# Generated by Django 3.0.7 on 2020-06-26 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0009_auto_20200622_1619'),
        ('fac', '0010_auto_20200622_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.Cliente')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='FacturDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.FacturaEnc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Producto')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Factura',
                'verbose_name_plural': 'Detalles Facturas',
            },
        ),
    ]
