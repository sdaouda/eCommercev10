# Generated by Django 4.1.2 on 2022-11-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immoapp', '0007_alter_clientalert_commentaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientalert',
            name='slug',
        ),
    ]
