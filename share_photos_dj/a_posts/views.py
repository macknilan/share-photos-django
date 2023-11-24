"""Posts views."""
from django.shortcuts import render, redirect
from share_photos_dj.a_posts.models import Post
from share_photos_dj.a_posts.forms.forms_posts import PostCreateFrom


def home_view(request):
    """Home view."""
    posts = Post.objects.all()
    return render(request, "a_posts/home.html", {"posts": posts})


def post_create_view(request):
    """Post create view."""

    if request.method == "POST":
        form = PostCreateFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostCreateFrom()

    return render(request, "a_posts/post_create.html", {"form": form})
