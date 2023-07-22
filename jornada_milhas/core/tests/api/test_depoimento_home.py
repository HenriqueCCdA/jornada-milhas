from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:post-home"


def test_possitive(client_api, posts):
    url = resolve_url(URL)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    assert len(body["results"]) == 3
