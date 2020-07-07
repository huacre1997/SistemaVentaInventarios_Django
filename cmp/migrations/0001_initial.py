# Generated by Django 3.0.7 on 2020-06-12 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('updatedUsu', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('contacto', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('createdUsu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]