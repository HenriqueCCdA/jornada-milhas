import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Destination

URL = "core:destination-list-create"


def test_positive_list(client_api, payload_destination, db):
    url = resolve_url(URL)

    resp = client_api.post(url, data=payload_destination, format="multipart")

    body = resp.json()

    assert resp.status_code == status.HTTP_201_CREATED

    assert Destination.objects.exists()

    destination_db = Destination.objects.all()[0]

    assert body["id"] == destination_db.pk
    assert body["name"] == destination_db.name
    assert body["price"] == str(destination_db.price)
    assert body["photo1"] == f"http://testserver{destination_db.photo1.url}"
    assert body["photo2"] == f"http://testserver{destination_db.photo2.url}"
    assert body["meta"] == destination_db.meta


@pytest.mark.parametrize(
    "field, error",
    [
        ("name", ["Este campo é obrigatório."]),
        ("price", ["Este campo é obrigatório."]),
        ("photo1", ["Nenhum arquivo foi submetido."]),
        ("photo2", ["Nenhum arquivo foi submetido."]),
        ("meta", ["Este campo é obrigatório."]),
    ],
    ids=["name", "price", "photo1", "photo2", "meta"],
)
def test_negative_missing_fields(client_api, destination, field, error):
    url = resolve_url(URL)

    data = {
        "name": destination.name,
        "price": destination.price,
        "photo1": destination.photo1.file,
        "photo2": destination.photo2.file,
        "meta": destination.meta,
    }

    del data[field]

    resp = client_api.post(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()
    assert body[field] == error


@pytest.mark.parametrize(
    "field, value, error",
    [
        ("price", "dd", "Um número válido é necessário."),
        ("price", -1.00, "Certifque-se de que este valor seja maior ou igual a 0.01."),
        ("photo1", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
        ("photo2", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["price-1", "price-2", "photo1", "photo2"],
)
def test_negative_validation_errors(client_api, field, destination, value, error):
    data = {
        "name": destination.name,
        "price": destination.price,
        "photo1": destination.photo1.file,
        "photo2": destination.photo2.file,
        "meta": destination.meta,
    }

    data[field] = value

    url = resolve_url(URL)

    resp = client_api.post(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()

    assert body[field] == [error]
