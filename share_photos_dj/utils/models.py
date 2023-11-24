# https://docs.djangoproject.com/en/3.2/topics/db/models/#model-inheritance

from django.db import models
from django.utils.translation import gettext_lazy as _


class RootBaseModel(models.Model):
    """
    RootBase BASE MODEL.
    THIS MODEL ACT AS ABSTRACT MODEL AND DEFINE FIELDS THAT ALL OTHERS
    MODELS IN THE APPLICATION MUST TO HAVE.
    """

    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("Date time at which an object was created"),
    )
    updated_at = models.DateTimeField(
        _("updated_at"),
        auto_now=True,
        help_text=_("Date time at which an object was modified"),
    )

    class Meta:
        """Meta option."""

        # https://docs.djangoproject.com/en/3.2/ref/models/options/#available-meta-options
        abstract = True

        get_latest_by = "created_at"
        ordering = ["-created_at", "-updated_at"]
