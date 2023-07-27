from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Destination

URL = "core:destination-retrieve-update-destroy"


def test_positive_delete(client_api, destination):
    url = resolve_url(URL, destination.pk)

    resp = client_api.delete(url)

    assert resp.status_code == status.HTTP_204_NO_CONTENT

    assert not Destination.objects.exists()


def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.delete(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
