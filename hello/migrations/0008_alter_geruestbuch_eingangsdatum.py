# Generated by Django 5.0.2 on 2024-02-18 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_geruestbuch_eingangsdatum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geruestbuch',
            name='Eingangsdatum',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Eingangsdatum'),
        ),
    ]