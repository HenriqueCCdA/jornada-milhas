from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Destination

URL = "core:destination-list-create"


def test_positive_list(client_api, destinations):
    url = resolve_url(URL)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    destination_db = Destination.objects.all()

    assert body["count"] == 6

    for from_db, from_response in zip(destination_db, body["results"]):
        assert from_db.id == from_response["id"]
        assert from_db.name == from_response["name"]
        assert str(from_db.price) == from_response["price"]
        assert f"http://testserver{from_db.photo.url}" == from_response["photo"]


def test_negative_invalid_page_pagination(client_api, destinations):
    url = resolve_url(URL)

    resp = client_api.get(f"{url}?page=5")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    body = resp.json()

    assert body["detail"] == "Página inválida."
