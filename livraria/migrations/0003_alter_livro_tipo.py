# Generated by Django 4.2.2 on 2023-07-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0002_alter_editora_options_alter_livro_options_livro_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Paperback', 'Paperback'), ('Hardcover', 'Hardcover')], default='Paperback', max_length=20, null=True),
        ),
    ]
