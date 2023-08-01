import pytest
from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:post-retrieve-update-destroy"


@pytest.mark.integration
def test_positive_update(client_api, post, new_photo, new_user):
    url = resolve_url(URL, post.pk)

    data = {
        "statement": "new statement",
        "user": new_user.pk,
        "photo": new_photo,
    }

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_200_OK
    # check DB
    post.refresh_from_db()
    assert post.statement == "new statement"

    body = resp.json()
    assert body["statement"] == "new statement"
    assert body["user"] == new_user.pk
    assert body["photo"] == f"http://testserver/media/post/{new_photo.name}"


@pytest.mark.integration
@pytest.mark.parametrize(
    "field, error",
    [
        ("statement", ["Este campo é obrigatório."]),
        ("user", ["Este campo é obrigatório."]),
        ("photo", ["Nenhum arquivo foi submetido."]),
    ],
    ids=["statement", "user", "photo"],
)
def test_negative_missing_fields(client_api, post, field, error):
    url = resolve_url(URL, post.pk)

    data = {
        "statement": post.statement,
        "user": post.user.pk,
        "photo": post.photo.file,
    }

    del data[field]

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()
    assert body[field] == error


@pytest.mark.integration
@pytest.mark.parametrize(
    "field, value, error",
    [
        ("user", "ab", "Tipo incorreto. Esperado valor pk, recebeu str."),
        ("user", 444, 'Pk inválido "444" - objeto não existe.'),
        ("photo", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["user-1", "user-2", "photo"],
)
def test_negative_validation_errors(client_api, field, post, value, error):
    data = {
        "statement": post.statement,
        "user": post.user.pk,
        "photo": post.photo.file,
    }

    data[field] = value

    url = resolve_url(URL, post.pk)

    resp = client_api.put(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()

    assert body[field] == [error]


@pytest.mark.integration
def test_negative_not_found(client_api, db):
    url = resolve_url(URL, 404)

    resp = client_api.put(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert body == {"detail": "Não encontrado."}
