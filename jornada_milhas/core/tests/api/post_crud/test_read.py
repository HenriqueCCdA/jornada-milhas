import pytest
from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:post-retrieve-update-destroy"


@pytest.mark.integration
def test_positive_read(client_api, post):
    url = resolve_url(URL, post.pk)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    assert body["id"] == post.pk
    assert body["statement"] == post.statement
    assert body["user"] == post.user.pk
    assert body["photo"] == f"http://testserver{post.photo.url}"


@pytest.mark.integration
def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
