# Generated by Django 3.0.7 on 2020-06-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0009_auto_20200621_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Jurídica', 'Jurídica'), ('Natural', 'Natural')], default='Natural', max_length=10),
        ),
    ]