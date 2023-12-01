"""Posts views."""
from django.shortcuts import render, redirect
from share_photos_dj.a_posts.models import Post
from share_photos_dj.a_posts.forms.forms_posts import PostCreateFrom
from bs4 import BeautifulSoup
import requests


def home_view(request):
    """Home view."""
    posts = Post.objects.all()
    return render(request, "a_posts/home.html", {"posts": posts})


def post_create_view(request):
    """Post create view."""

    if request.method == "POST":
        form = PostCreateFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["image"])
            sourcecode = BeautifulSoup(website.text, "html.parser")
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')

            image = find_image[0]['content']
            post.image = image

            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist

            find_link = sourcecode.select('link')
            link = find_link[0].attrs["href"]
            post.link = link

            post.save()
            return redirect("home")
    else:
        form = PostCreateFrom()

    return render(request, "a_posts/post_create.html", {"form": form})
