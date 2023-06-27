from django.contrib import admin
from django.utils.html import format_html

from .models import Transfer


class TransferAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'route', 'auto')
    list_filter = ('date', 'auto', 'route')
    search_fields = ('name', 'auto', 'route')
    ordering = ('date',)


admin.site.register(Transfer, TransferAdmin)