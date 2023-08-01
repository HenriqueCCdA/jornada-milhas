import pytest
from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:destination-retrieve-update-destroy"


@pytest.mark.integration
def test_positive_read(client_api, destination):
    url = resolve_url(URL, destination.pk)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    assert body["id"] == destination.pk
    assert body["name"] == destination.name
    assert body["price"] == str(destination.price)
    assert body["photo1"] == f"http://testserver{destination.photo1.url}"
    assert body["photo2"] == f"http://testserver{destination.photo2.url}"
    assert body["meta"] == destination.meta
    assert body["describe"] is None


@pytest.mark.integration
def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
