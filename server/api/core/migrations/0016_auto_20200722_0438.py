# Generated by Django 3.0.8 on 2020-07-22 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200722_0257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtheme',
            old_name='item_size',
            new_name='size',
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]