# Generated by Django 4.0 on 2023-07-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaferramentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ferramenta',
            name='editora',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='isbn',
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='tipo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
