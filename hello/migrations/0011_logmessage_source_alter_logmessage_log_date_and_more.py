# Generated by Django 5.0.2 on 2024-02-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_alter_firma_options_alter_ansprechpartner_firma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='source',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='log_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date logged'),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
