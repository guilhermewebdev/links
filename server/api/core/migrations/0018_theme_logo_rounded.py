# Generated by Django 3.0.8 on 2020-07-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_theme_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='logo_rounded',
            field=models.IntegerField(default=0),
        ),
    ]
