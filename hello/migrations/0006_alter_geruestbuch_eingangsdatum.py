# Generated by Django 5.0.2 on 2024-02-18 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_inventar_projekt_geruestbuch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geruestbuch',
            name='Eingangsdatum',
            field=models.DateField(default=datetime.datetime(2024, 2, 18, 13, 6, 7, 319547, tzinfo=datetime.timezone.utc), verbose_name='Eingangsdatum'),
        ),
    ]