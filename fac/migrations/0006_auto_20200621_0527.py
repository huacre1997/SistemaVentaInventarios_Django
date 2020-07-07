# Generated by Django 3.0.7 on 2020-06-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0005_auto_20200621_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural', max_length=10),
        ),
    ]