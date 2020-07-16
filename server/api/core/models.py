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
    price = models.IntegerField(
        null=True,
        blank=True,
    )
    link = models.URLField(
        max_length=300
    )
    image = models.ImageField(
        upload_to='media/images/items/',
        null=True,
        blank=True,
    )
    store = models.ForeignKey(
        'Store',
        on_delete=models.CASCADE,
        related_name='items',
    )
    reference = models.SlugField(
        max_length=50,
        null=True,
        blank=True,
    )
    index = models.IntegerField()

    def __str__(self):
        return self.title

    @property
    def admin_url(self):
        return f'/{self.store.get_url()}/{self.reference}'

    class Meta:
        unique_together = (
            ('reference', 'store'),
            ('index', 'store'),
        )
        ordering = ['index']

class Store(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stores',
    )
    background_image = models.ImageField(
        upload_to='media/images/bg/',
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
    )
    background_color = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='#FFFFFF'
    )
    rounded = models.IntegerField(
        default=0,
    )
    logo = models.ImageField(
        upload_to='media/images/logos/',
        null=True,
        blank=True,
    )
    item_size = models.IntegerField(
        default=12,
    )
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

    def __str__(self):
        return self.title

    @property
    def items_admin_url(self):
        return f'/settings/{self.pk}/items/'

    @property
    def admin_url(self):
        return f'/settings/{self.pk}/'

    @property
    def url(self):
        return f'/{self.slug}'
