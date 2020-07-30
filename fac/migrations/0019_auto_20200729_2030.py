# Generated by Django 3.0.7 on 2020-07-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0018_auto_20200703_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='NAT', max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updatedUsu',
            field=models.IntegerField(blank=True, null=True, verbose_name='user.User'),
        ),
    ]