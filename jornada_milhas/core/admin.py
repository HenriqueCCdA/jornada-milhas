from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from jornada_milhas.core.models import Post


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


admin.site.register(Post, PostModelAdmin)
