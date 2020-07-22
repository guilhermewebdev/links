# Generated by Django 3.0.8 on 2020-07-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200716_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='background_header',
            field=models.CharField(default='transparent', max_length=15),
        ),
        migrations.AddField(
            model_name='store',
            name='description_color',
            field=models.CharField(default='#000', max_length=15),
        ),
        migrations.AddField(
            model_name='store',
            name='title_color',
            field=models.CharField(default='#000', max_length=15),
        ),
        migrations.AlterField(
            model_name='store',
            name='background_color',
            field=models.CharField(default='#FFFFFF', max_length=15),
        ),
    ]