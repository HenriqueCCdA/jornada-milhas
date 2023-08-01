import pytest
from django.shortcuts import resolve_url
from rest_framework import status

URL = "core:post-home"


@pytest.mark.integration
@pytest.mark.num_post(3)
def test_possitive(client_api, post):
    url = resolve_url(URL)

    resp = client_api.get(url)

    body = resp.json()

    assert resp.status_code == status.HTTP_200_OK

    assert len(body["results"]) == 3
