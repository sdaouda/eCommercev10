# Generated by Django 4.1.2 on 2022-11-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immoapp', '0008_remove_clientalert_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientalert',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]