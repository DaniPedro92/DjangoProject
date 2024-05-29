# Generated by Django 4.0 on 2023-07-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listaferramentas', '0002_remove_ferramenta_editora_remove_ferramenta_isbn_and_more'),
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('ferramenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listaferramentas.ferramenta')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.pessoa')),
            ],
        ),
    ]
