import pytest
from django.urls import reverse

from .factories import UserFactory


@pytest.fixture()
def user():
    return UserFactory.create()


@pytest.fixture()
def user_token(api_client, user):
    response = api_client.post(reverse("token_obtain_pair"), {"username": user.username, "password": "yT-123?ab"})
    return user, f"Bearer {response.json()['access']}"


@pytest.fixture()
def authorized_api_client(api_client, user_token):
    user, token = user_token
    api_client.force_authenticate(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=token)
    return api_client
