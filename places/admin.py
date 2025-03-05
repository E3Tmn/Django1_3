from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview_image']
    ordering = ['order', ]

    def get_preview_image(self, obj):
        width = '150px'
        height = '150px'
        return format_html(
            '<img src="{}" max-width={} height={}/>',
            obj.image.url,
            width,
            height)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
