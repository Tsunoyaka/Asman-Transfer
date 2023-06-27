from django.contrib import admin
from django.utils.html import format_html

from .models import Auto, Driver


class AutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'contract_price', 'capacity', 'display_image')
    list_filter = ('title', 'price', 'contract_price', 'capacity')
    search_fields = ('title',)
    ordering = ('price', 'capacity')
    readonly_fields = ('display_image',) 

    def display_image(self, obj):
        return format_html('<img src="{}" width="250" height="200" />', obj.photo.url)

    display_image.short_description = 'Изображение'


class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'display_image')
    readonly_fields = ('display_image',) 


    def display_image(self, obj):
        return format_html('<img src="{}" width="250" height="200" />', obj.photo.url)

    display_image.short_description = 'Изображение'

admin.site.register(Auto, AutoAdmin)
admin.site.register(Driver, DriverAdmin)
