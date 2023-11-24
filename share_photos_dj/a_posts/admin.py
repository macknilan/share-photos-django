"""Post models admin."""

from django.contrib import admin

# Models
from share_photos_dj.a_posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile model admin"""

    list_display = [
        "id",
        "title",
        "body",
        "image",
        "is_draft",
        "url",
        "publish_date",
    ]
    search_fields = [
        "title",
        "publish_date",
    ]
    list_filter = [
        "is_draft",
        "publish_date",
    ]
    list_display_links = [
        "id",
        "title",
    ]
    list_editable = [
        "is_draft",
    ]
