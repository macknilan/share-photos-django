"""
Forms for the posts app
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError

from share_photos_dj.a_posts.models import Post


class PostCreateFrom(ModelForm):
    """
    Post create form.
    """

    def clean_title(self):
        """Validate title."""
        data = self.cleaned_data["title"]
        if len(data) < 10:
            raise ValidationError(_("The title is too short"))
        return data

    class Meta:
        model = Post
        fields = [
            # "title",
            "body",
            "image"
        ]
        labels = {
            # "title":  _("Title"),
            "body": _("Body"),
            "image": _("Image"),
        }
        widgets = {
            # "title": forms.TextInput(attrs={"required": True, "placeholder": "write a title ...", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "body": forms.Textarea(attrs={"required": True, "placeholder": "write a body ..", "rows": 3, "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "image": forms.TextInput(attrs={"required": True, "placeholder": "write a url image ..", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        }
        error_messages = {
            # "title": {
            #     "required": _("Title is required"),
            # },
            "body": {
                "required": _("Body is required"),
            },
            "image": {
                "required": _("Image url is required"),
            },
        }

