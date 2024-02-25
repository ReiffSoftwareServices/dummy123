# Generated by Django 5.0.2 on 2024-02-18 13:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_firma_options_firma_email_firma_postleitzahl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Bauteil')),
                ('Einheit', models.CharField(max_length=50, verbose_name='Einheit')),
                ('Beschreibung', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('Preis', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Preis')),
                ('Einheit_Miete', models.CharField(max_length=50, verbose_name='Einheit Miete')),
                ('Beschreibung_Miete', models.CharField(max_length=50, verbose_name='Beschreibung Miete')),
                ('Preis_Miete', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Preis Miete')),
            ],
            options={
                'verbose_name_plural': 'Leistungsverzeichnis',
            },
        ),
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('Project_Name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Projekt Name')),
            ],
            options={
                'verbose_name_plural': 'Projekte',
            },
        ),
        migrations.CreateModel(
            name='Geruestbuch',
            fields=[
                ('Geruestnummer', models.AutoField(primary_key=True, serialize=False)),
                ('Grund', models.TextField(blank=True, verbose_name='Grund')),
                ('Anlage', models.CharField(blank=True, max_length=100, verbose_name='Anlage/ Equipment')),
                ('Ebene', models.CharField(blank=True, max_length=100, verbose_name='Ebene')),
                ('Oertlichkeit', models.CharField(blank=True, max_length=100, verbose_name='Oertlichkeit')),
                ('Eingangsdatum', models.DateField(default=datetime.date(2024, 2, 18), verbose_name='Eingangsdatum')),
                ('Aufbaudatum', models.DateField(blank=True, null=True, verbose_name='Aufbaudatum')),
                ('Abmeldedatum', models.DateField(blank=True, null=True, verbose_name='Abmeldedatum')),
                ('Mietbeginn', models.DateField(blank=True, null=True, verbose_name='Miet-Beginn')),
                ('Mietende', models.DateField(blank=True, null=True, verbose_name='Miet-Ende')),
                ('Preis', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Preis')),
                ('Ansprechpartner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.ansprechpartner', verbose_name='Ansprechpartner')),
                ('Kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.firma', verbose_name='Firma')),
                ('Projekt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.projekt', verbose_name='Projekt Name')),
            ],
            options={
                'verbose_name_plural': 'Geruestbuch',
            },
        ),
    ]