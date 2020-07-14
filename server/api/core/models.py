from django.db import models
from django.contrib.auth import get_user_model


class Item(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    price = models.IntegerField()
    link = models.URLField(
        max_length=300
    )
    image = models.ImageField(
        upload_to='media/images/itens'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    reference = models.CharField(
        max_length=50,
    )

    class Meta:
        unique_together = ('reference', 'owner')


class Store(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    background_image = models.ImageField(
        upload_to='media/images/bg',
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=150,
    )
    background_color = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='#FFFFFF'
    )
    rounded = models.IntegerField()
    logo = models.ImageField(
        upload_to='media/images/bg',
        null=True,
        blank=True,
    )
    item_size = models.IntegerField()
    font = models.CharField(
        max_length=30,
        default="Helvetica",
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    pixel = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    analytics = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
