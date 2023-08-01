import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Post

URL = "core:post-retrieve-update-destroy"


@pytest.mark.integration
def test_positive_delete(client_api, post):
    url = resolve_url(URL, post.pk)

    resp = client_api.delete(url)

    assert resp.status_code == status.HTTP_204_NO_CONTENT

    assert not Post.objects.exists()


@pytest.mark.integration
def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.delete(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
