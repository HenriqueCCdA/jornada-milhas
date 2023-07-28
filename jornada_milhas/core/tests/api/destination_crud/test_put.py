from decimal import Decimal

import pytest
from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:destination-retrieve-update-destroy"


def test_positive_update(client_api, destination, new_photo):
    url = resolve_url(URL, destination.pk)

    data = {
        "name": "New name",
        "price": "30.10",
        "photo": new_photo,
    }

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_200_OK
    # check DB
    destination.refresh_from_db()
    assert destination.name == "New name"
    assert destination.price == Decimal("30.10")

    body = resp.json()
    assert body["name"] == "New name"
    assert body["price"] == "30.10"
    assert body["photo"] == f"http://testserver/media/destination/{new_photo.name}"


@pytest.mark.parametrize(
    "field, error",
    [
        ("name", ["Este campo é obrigatório."]),
        ("price", ["Este campo é obrigatório."]),
        ("photo", ["Nenhum arquivo foi submetido."]),
    ],
    ids=["name", "price", "photo"],
)
def test_negative_missing_fields(client_api, destination, field, error):
    url = resolve_url(URL, destination.pk)

    data = {
        "name": destination.name,
        "price": destination.price,
        "photo": destination.photo.file,
    }

    del data[field]

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()
    assert body[field] == error


@pytest.mark.parametrize(
    "field, value, error",
    [
        ("price", "dd", "Um número válido é necessário."),
        ("price", -1.00, "Certifque-se de que este valor seja maior ou igual a 0.01."),
        ("photo", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["price-1", "price-2", "photo"],
)
def test_negative_validation_errors(client_api, field, destination, value, error):
    data = {
        "name": destination.name,
        "price": destination.price,
        "photo": destination.photo.file,
    }

    data[field] = value

    url = resolve_url(URL, destination.pk)

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()

    assert body[field] == [error]


def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.put(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
