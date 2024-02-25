# Generated by Django 5.0.2 on 2024-02-18 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_equipments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firma',
            options={'verbose_name_plural': 'Firmenliste'},
        ),
        migrations.AlterField(
            model_name='ansprechpartner',
            name='Firma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.firma', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='Equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.inventar', verbose_name='Inventar'),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='Geruestnummer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.geruestbuch', verbose_name='Geruestnummer'),
        ),
        migrations.AlterField(
            model_name='geruestbuch',
            name='Ansprechpartner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.ansprechpartner', verbose_name='Ansprechpartner'),
        ),
        migrations.AlterField(
            model_name='geruestbuch',
            name='Kunde',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.firma', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='geruestbuch',
            name='Projekt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.projekt', verbose_name='Projekt Name'),
        ),
    ]
