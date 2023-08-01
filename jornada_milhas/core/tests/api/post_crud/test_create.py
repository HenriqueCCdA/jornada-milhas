import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Post

URL = "core:post-list-create"


@pytest.mark.integration
def test_positive_list(client_api, payload_post):
    url = resolve_url(URL)

    resp = client_api.post(url, data=payload_post, format="multipart")

    body = resp.json()

    assert resp.status_code == status.HTTP_201_CREATED

    assert Post.objects.exists()

    post_db = Post.objects.all()[0]

    assert body["id"] == post_db.pk
    assert body["photo"] == f"http://testserver{post_db.photo.url}"
    assert body["statement"] == post_db.statement
    assert body["user"] == post_db.user.pk


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
    url = resolve_url(URL)

    data = {
        "statement": post.statement,
        "user": post.user.pk,
        "photo": post.photo.file,
    }

    del data[field]

    resp = client_api.post(url, data=data, format="multipart")

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

    url = resolve_url(URL)

    resp = client_api.post(url, data=data, format="multipart")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    body = resp.json()

    assert body[field] == [error]
