# Generated by Django 4.2.2 on 2023-06-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('realizado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
