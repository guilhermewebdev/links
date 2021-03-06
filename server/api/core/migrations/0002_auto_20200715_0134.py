# Generated by Django 3.0.8 on 2020-07-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['index']},
        ),
        migrations.AddField(
            model_name='item',
            name='index',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('index', 'store'), ('reference', 'store')},
        ),
    ]
