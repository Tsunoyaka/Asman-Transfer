from django.contrib import admin
from django.utils.html import format_html

from .models import Recall, Documentation, Video, DefaultUserImage

class RecallAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ('rating',)
    search_fields = ('title',)
    ordering = ('rating',)
    readonly_fields = ('display_image',) 

    def display_image(self, obj):
        return format_html('<img src="{}" width="250" height="200" />', obj.photo.url)

    display_image.short_description = 'Изображение'


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')
    readonly_fields = ('display_image',) 

    def display_image(self, obj):
        return format_html('<img src="{}" width="250" height="200" />', obj.photo.url)
    
    display_image.short_description = 'Изображение'


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video')


admin.site.register(Recall, RecallAdmin)
admin.site.register(Documentation, DocumentationAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(DefaultUserImage)