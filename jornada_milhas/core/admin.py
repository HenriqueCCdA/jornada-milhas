from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from jornada_milhas.core.models import Destination, Post


class PostModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("id",)},
        ),
        (
            _("Post data"),
            {
                "fields": (
                    "photo",
                    "user",
                    "statement",
                )
            },
        ),
        (_("Important dates"), {"fields": ("created_at", "modified_at")}),
    )

    list_display = (
        "id",
        "user",
        "statement",
        "created_at",
        "modified_at",
    )

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


class DestinationModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("id",)},
        ),
        (
            _("Post data"),
            {
                "fields": (
                    "photo1",
                    "photo2",
                    "meta",
                    "describe",
                    "name",
                    "price",
                )
            },
        ),
        (_("Important dates"), {"fields": ("created_at", "modified_at")}),
    )

    list_display = (
        "id",
        "name",
        "price",
        "created_at",
        "modified_at",
    )

    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )


admin.site.register(Post, PostModelAdmin)
admin.site.register(Destination, DestinationModelAdmin)
