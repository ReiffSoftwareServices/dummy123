# Generated by Django 5.0.2 on 2024-02-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_alter_logmessage_message_alter_logmessage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geruestbuch',
            name='Geruestnummer',
            field=models.AutoField(help_text='Name der Person, welche dsa Gerüst anfordert.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='log_date',
            field=models.DateTimeField(blank=True, help_text='yxcv', null=True, verbose_name='date logged'),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='message',
            field=models.CharField(blank=True, help_text='xxx', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='name',
            field=models.CharField(blank=True, help_text='yyy', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logmessage',
            name='source',
            field=models.CharField(blank=True, help_text='yyx', max_length=2, null=True),
        ),
    ]
