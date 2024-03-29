# Generated by Django 5.0.2 on 2024-02-18 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_alter_geruestbuch_eingangsdatum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Laenge', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Laenge')),
                ('Breite', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Breite')),
                ('Hoehe', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Hoehe')),
                ('Stueck', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Stueck')),
                ('Stunde', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Stunde')),
                ('Equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.inventar', verbose_name='Inventar')),
                ('Geruestnummer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.geruestbuch', verbose_name='Geruestnummer')),
            ],
            options={
                'verbose_name_plural': 'Equipment',
            },
        ),
    ]
