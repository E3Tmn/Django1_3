from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

admin.site.register(Image)


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview_image']
    ordering = ['order', ]

    def get_preview_image(self, obj):
        width = '150px'
        return format_html(f'<img src="{obj.image.url}" max-width={width} />')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
