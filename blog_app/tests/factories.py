import random

import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from factory import fuzzy

from .. import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password("yT-123?ab"))


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    user = factory.SubFactory(UserFactory)
    title = fuzzy.FuzzyText(length=50)
    text = fuzzy.FuzzyText(length=random.randint(100, 500))
