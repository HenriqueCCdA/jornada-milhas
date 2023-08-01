import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Post

URL = "core:post-list-create"


@pytest.mark.num_post(5)
@pytest.mark.integration
def test_positive_list(client_api, post):
    url = resolve_url(URL)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    posts_db = Post.objects.all()

    assert body["count"] == 5

    for from_db, from_response in zip(posts_db, body["results"], strict=True):
        assert from_db.id == from_response["id"]
        assert from_db.statement == from_response["statement"]
        assert from_db.user.pk == from_response["user"]
        assert f"http://testserver{from_db.photo.url}" == from_response["photo"]


@pytest.mark.num_post(4)
@pytest.mark.integration
def test_negative_invalid_page_pagination(client_api, post):
    url = resolve_url(URL)

    resp = client_api.get(f"{url}?page=5")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    body = resp.json()

    assert body["detail"] == "Página inválida."
