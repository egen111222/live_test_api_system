# Generated by Django 3.1.7 on 2021-07-09 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_module', '0002_auto_20210709_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='good',
            new_name='goods',
        ),
    ]
