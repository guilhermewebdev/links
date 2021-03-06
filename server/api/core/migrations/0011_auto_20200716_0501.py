# Generated by Django 3.0.8 on 2020-07-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200716_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/items/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/bg/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/logos/'),
        ),
    ]
