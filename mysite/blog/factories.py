# SeuApp/tests/factories.py

import factory
from faker import Faker
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from blog.models import Post

faker = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    slug = factory.LazyAttribute(lambda obj: f"post-{obj.title}")
    author = factory.SubFactory(UserFactory)
    content = faker.paragraph()
    status = 0
