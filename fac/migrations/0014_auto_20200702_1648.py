# Generated by Django 3.0.7 on 2020-07-02 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0013_auto_20200702_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaenc',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]