from django.contrib import admin
from . import models

class ItemInline(admin.StackedInline):
    model = models.Item
    extra = 1
    ordering = ('index',)

@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]


@admin.register(models.ItemTheme)
class ItemThemeAdmin(admin.ModelAdmin):
    pass

class ItemThemeInline(admin.StackedInline):
    model = models.ItemTheme

@admin.register(models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [
        ItemThemeInline
    ]