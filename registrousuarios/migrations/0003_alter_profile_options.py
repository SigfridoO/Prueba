# Generated by Django 3.2.6 on 2021-09-11 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrousuarios', '0002_profile_saldo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user'], 'verbose_name': 'perfil de usuario', 'verbose_name_plural': 'perfiles de usuario'},
        ),
    ]
