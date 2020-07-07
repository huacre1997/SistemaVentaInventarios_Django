# Generated by Django 3.0.7 on 2020-07-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0014_auto_20200702_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaenc',
            name='nrofactura',
            field=models.BigIntegerField(blank=None, default=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural', max_length=10),
        ),
    ]