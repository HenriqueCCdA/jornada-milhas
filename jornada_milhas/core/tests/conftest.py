import io

import pytest
from django.core.files.base import ContentFile
from model_bakery import baker
from PIL import Image
from rest_framework.test import APIClient

from jornada_milhas.core.models import Post


@pytest.fixture(autouse=True)
def mediafiles(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path / "media"


@pytest.fixture
def client_api():
    return APIClient()


@pytest.fixture
def photo():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.seek(0)
    return ContentFile(file.read(), name="photo.png")


@pytest.fixture
def new_photo():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.seek(0)
    return ContentFile(file.read(), name="new_photo.png")


@pytest.fixture
def post(photo, db):
    return baker.make(Post, photo=photo)


@pytest.fixture
def posts(photo, db):
    return baker.make(Post, _quantity=5, photo=photo)


@pytest.fixture
def payload_post(user, photo):
    return {
        "photo": photo,
        "statement": "New",
        "user": user.pk,
    }
