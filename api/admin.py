from django.contrib import admin
from .models import Friend

admin.site.site_title = "AI Friend Application"


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ("name", "prompt", "created_at")
    search_fields = ("name",)
