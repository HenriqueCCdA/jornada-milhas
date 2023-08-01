from django.shortcuts import resolve_url
from model_bakery import baker
from rest_framework import status

from jornada_milhas.core.models import Destination

URL = "core:destination-list-create"


def test_positive_list(client_api, destinations):
    url = resolve_url(URL)

    resp = client_api.get(url)

    assert resp.status_code == status.HTTP_200_OK

    destination_db = Destination.objects.all()

    body = resp.json()

    assert body["count"] == 6

    for from_db, from_response in zip(destination_db, body["results"], strict=True):
        assert from_db.id == from_response["id"]
        assert from_db.name == from_response["name"]
        assert str(from_db.price) == from_response["price"]
        assert f"http://testserver{from_db.photo1.url}" == from_response["photo1"]
        assert f"http://testserver{from_db.photo2.url}" == from_response["photo2"]
        assert f"http://testserver{from_db.photo2.url}" == from_response["photo2"]
        assert from_db.meta == from_response["meta"]


def test_positive_list_query_param(client_api, photo, photo2, db):
    url = resolve_url(URL)

    baker.make(Destination, name="Brasil", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Bahamas", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Barbados", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Ruanda", photo1=photo, photo2=photo2)

    resp = client_api.get(f"{url}?name=Ba")

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert body["count"] == 2


def test_positive_list_query_param_not_found(client_api, photo, photo2, db):
    url = resolve_url(URL)

    baker.make(Destination, name="Brasil", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Bahamas", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Barbados", photo1=photo, photo2=photo2)
    baker.make(Destination, name="Ruanda", photo1=photo, photo2=photo2)

    resp = client_api.get(f"{url}?name=Fa")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    body = resp.json()

    assert body["mensagem"] == "Nenhum destino foi encontrado."


def test_negative_invalid_page_pagination(client_api, destinations):
    url = resolve_url(URL)

    resp = client_api.get(f"{url}?page=5")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    body = resp.json()

    assert body["detail"] == "Página inválida."
