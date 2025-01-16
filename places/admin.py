from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.utils.html import format_html

# Register your models here.
admin.site.register(Image)
class ImageInline(SortableStackedInline):
    model = Image

    readonly_fields = ["preview_image"]
    ordering = ['order',]

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150px" />')

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    

    