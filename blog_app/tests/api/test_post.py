import pytest
from django.urls import reverse

from ..factories import PostFactory


@pytest.mark.django_db
@pytest.mark.parametrize("batch_size", range(10, 100, 25))
def test_post_list(authorized_api_client, batch_size: int):
    PostFactory.create_batch(batch_size)
    response = authorized_api_client.get(reverse("post-list"), format="json")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["count"] == batch_size


@pytest.mark.django_db
def test_get_post_detail(authorized_api_client):
    post = PostFactory.create()
    response = authorized_api_client.get(reverse("post-detail", kwargs={"pk": post.id}), format="json")
    assert response.status_code == 200
    response_data = response.json()
    assert post.id == response_data["id"]
