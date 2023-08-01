# SeuApp/tests/test_models.py

import pytest
from blog.models import Post
from blog.factories import PostFactory

@pytest.mark.django_db
def test_create_post():
    post = PostFactory()
    assert isinstance(post, Post)
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_create_published_post():
    post = PostFactory(status=1)
    assert isinstance(post, Post)
    assert Post.objects.filter(status=1).count() == 1
