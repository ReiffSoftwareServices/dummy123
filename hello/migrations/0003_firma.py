# Generated by Django 5.0.2 on 2024-02-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_logmessage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]
