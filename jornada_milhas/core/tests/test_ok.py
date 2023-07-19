from django.shortcuts import resolve_url
from rest_framework import status


def test_ok(client):
    url = resolve_url("core:root")

    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
