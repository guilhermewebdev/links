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
        upload_to='images/items/',
        null=True,
        blank=True,
    )
    size = models.IntegerField(
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
    theme = models.ForeignKey(
        'ItemTheme',
        on_delete=models.DO_NOTHING,
        related_name='items',
        null=True,
        blank=True,
    )

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
        upload_to='images/bg/',
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
    )
    logo = models.ImageField(
        upload_to='images/logos/',
        null=True,
        blank=True,
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
    theme = models.ForeignKey(
        'Theme',
        on_delete=models.DO_NOTHING,
        related_name='stores',
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


class AbstractTheme(models.Model):
    
    font_description = models.CharField(
        max_length=30,
        default="Helvetica",
    )
    font_title = models.CharField(
        max_length=30,
        default="Helvetica",
    )
    title_color = models.CharField(
        max_length=15,
        default='#000'
    )
    description_color = models.CharField(
        max_length=15,
        default='#000'
    )
    background_color = models.CharField(
        max_length=15,
        default='transparent'
    )

    class Meta:
        abstract = True

class ItemTheme(AbstractTheme):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='item_themes',
    ) 
    rounded = models.IntegerField(
        default=0,
    )
    item_size = models.IntegerField(
        default=12,
    )
    image_position = models.CharField(
        max_length=15,
        default='top',
    )
    padding = models.IntegerField(
        default=15,
    )
    border_color = models.CharField(
        max_length=15,
        default='#FFFFFF'
    )
    border_size = models.IntegerField(
        default=1,
    )
    border_style = models.CharField(
        max_length=20,
        default='solid'
    )

    class Meta:
        abstract = False


class StoreTheme(AbstractTheme):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='store_themes',
    ) 
    background_header = models.CharField(
        max_length=15,
        default='transparent'
    )
    logo_position = models.CharField(
        max_length=15,
        default='right',
    )

    class Meta:
        abstract = False


class Theme(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='themes',
    )
    store = models.ForeignKey(
        StoreTheme,
        on_delete=models.DO_NOTHING,
        related_name='themes',
    )
    items = models.ForeignKey(
        ItemTheme,
        on_delete=models.DO_NOTHING,
        related_name='themes',
    )