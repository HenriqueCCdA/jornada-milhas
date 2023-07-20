from django.shortcuts import resolve_url
from rest_framework import status

from jornada_milhas.core.models import Post

URL = "core:post-list-create"


def test_positive_list(client_api, posts):
    url = resolve_url(URL)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    posts_db = Post.objects.all()

    assert body["count"] == 3

    for e, r in zip(posts_db, body["results"]):
        assert e.id == r["id"]
        assert e.statement == r["statement"]
        assert e.user.pk == r["user"]
        assert f"http://testserver{e.photo.url}" == r["photo"]


def test_negative_invalid_page_pagination(client_api, posts):
    url = resolve_url(URL)

    resp = client_api.get(f"{url}?page=5")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    body = resp.json()

    assert body["detail"] == "Página inválida."
