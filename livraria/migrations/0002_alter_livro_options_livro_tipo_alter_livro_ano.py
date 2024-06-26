# Generated by Django 4.2.2 on 2023-07-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livro',
            options={'ordering': ['titulo']},
        ),
        migrations.AddField(
            model_name='livro',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Paperback', 'Paperback'), ('Hardcover', 'Hardcover')], default='Paperback', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='ano',
            field=models.SmallIntegerField(blank=True, default=2023, null=True),
        ),
    ]
