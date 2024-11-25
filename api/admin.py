from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "short_code", "access_count", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("url", "short_code")
    exclude = ("short_code",)
    ordering = ("-created_at",)
