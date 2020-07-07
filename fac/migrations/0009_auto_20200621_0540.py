# Generated by Django 3.0.7 on 2020-06-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0008_auto_20200621_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(error_messages={'unique': 'Please enter your name'}, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural', max_length=10),
        ),
    ]