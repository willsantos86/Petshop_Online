# Generated by Django 4.1.7 on 2023-03-14 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contatos'},
        ),
    ]
