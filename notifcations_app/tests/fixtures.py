import pytest
from rest_framework.test import APIClient

from .factories import NotificationFactory


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def notification_instance():
    return NotificationFactory.create()
