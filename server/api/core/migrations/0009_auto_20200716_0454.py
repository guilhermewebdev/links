# Generated by Django 3.0.8 on 2020-07-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='font',
            new_name='font_description',
        ),
        migrations.AddField(
            model_name='store',
            name='font_title',
            field=models.CharField(default='Helvetica', max_length=30),
        ),
    ]
