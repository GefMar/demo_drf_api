import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_notification(api_client, notification_instance):
    api_client.get(reverse("notification-list"), format="json")
