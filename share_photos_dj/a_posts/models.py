""" Model Post for the Blog """
import uuid

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Utilities
from share_photos_dj.utils.models import RootBaseModel


# https://docs.djangoproject.com/en/3.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
class PostLet(models.Manager):
    def get_queryset(self):
        """Show posts less than or equal to (lte) now"""
        now = timezone.now()
        return super().get_queryset().filter(publish_date__lte=now)


class Post(RootBaseModel):
    """Post model."""

    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(_("title"), max_length=255)
    body = models.TextField()
    image = models.URLField(_("url_image"), max_length=500, blank=True, null=True)
    is_draft = models.BooleanField(_("is_draft"), default=False)
    publish_date = models.DateTimeField(_("published_date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    url = models.SlugField(_("url"), max_length=255, null=True, blank=True)  # unique=True
    objects = models.Manager()  # The default manager
    published = PostLet()  # The Post Manager manager

    class Meta(RootBaseModel.Meta):
        """Overwrite meta class of RootBaseModel"""

        # ordering = ("title",)
        ordering = [
            "-created_at"
        ]

    def __str__(self):
        """Return title and username."""
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
