from django.contrib import admin
from . import models

class AdminSite(admin.AdminSite):
    site_title = 'Linkz'
    site_header = 'Linkz Administration'

admin.site = AdminSite(name='linkz')
admin.sites.site = admin.site

class SetOwner(admin.ModelAdmin):
    exclude = ('owner',)

    def save_model(self, request, obj, *args, **kwargs):
        obj.owner = request.user
        super().save_model(request, obj, *args, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def has_view_permission(self, request, obj=None):
        if obj: return request.user == obj.owner
        return True

    def has_change_permission(self, request, obj=None):
        if obj: return request.user == obj.owner
        return True

    def has_delete_permission(self, request, obj=None):
        if obj: return request.user == obj.owner
        return True

class ItemInline(admin.StackedInline):
    model = models.Item
    extra = 1
    ordering = ('index',)

@admin.register(models.Store)
class StoreAdmin(SetOwner):
    inlines = [
        ItemInline,
    ]


@admin.register(models.ItemTheme)
class ItemThemeAdmin(SetOwner):
    pass

class ItemThemeInline(admin.StackedInline):
    model = models.ItemTheme
    exclude = ('owner',)
    def save_model(self, request, obj, *args, **kwargs):
        obj.owner = request.user
        super().save_model(request, obj, *args, **kwargs)

@admin.register(models.Theme)
class ThemeAdmin(SetOwner):
    inlines = [
        ItemThemeInline
    ]

