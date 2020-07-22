# Generated by Django 3.0.8 on 2020-07-22 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200722_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='store',
        ),
        migrations.AddField(
            model_name='theme',
            name='background_color',
            field=models.CharField(default='transparent', max_length=15),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_header',
            field=models.CharField(default='transparent', max_length=15),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/bg/'),
        ),
        migrations.AddField(
            model_name='theme',
            name='description_color',
            field=models.CharField(default='#000', max_length=15),
        ),
        migrations.AddField(
            model_name='theme',
            name='font_description',
            field=models.CharField(default='Helvetica', max_length=30),
        ),
        migrations.AddField(
            model_name='theme',
            name='font_title',
            field=models.CharField(default='Helvetica', max_length=30),
        ),
        migrations.AddField(
            model_name='theme',
            name='logo_position',
            field=models.CharField(default='right', max_length=15),
        ),
        migrations.AddField(
            model_name='theme',
            name='title_color',
            field=models.CharField(default='#000', max_length=15),
        ),
        migrations.AlterField(
            model_name='theme',
            name='items',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ItemTheme'),
        ),
        migrations.DeleteModel(
            name='StoreTheme',
        ),
    ]
