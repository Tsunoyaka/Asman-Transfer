from django.contrib import admin

from django.utils.html import format_html

from .models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'promotion', 'display_image')
    search_fields = ('title',)
    readonly_fields = ('display_image',) 

    def display_image(self, obj):
        return format_html('<img src="{}" width="250" height="200" />', obj.photo.url)

    display_image.short_description = 'Изображение'


admin.site.register(Route, RouteAdmin)
