# Generated by Django 5.1.2 on 2024-12-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='driver',
            new_name='user',
        ),
    ]
