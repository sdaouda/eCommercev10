# Generated by Django 4.1.2 on 2022-11-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immoapp', '0002_rename_adresse_client_fullname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='adressemail',
        ),
        migrations.AlterField(
            model_name='client',
            name='cellphone_number',
            field=models.CharField(max_length=25),
        ),
    ]
