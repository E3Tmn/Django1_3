from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html

# Register your models here.
admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150px" />')
    

@admin.register(Place)
class ImageAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    