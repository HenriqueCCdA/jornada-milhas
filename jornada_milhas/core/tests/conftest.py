import io

import pytest
from django.core.files.base import ContentFile
from model_bakery import baker
from PIL import Image
from rest_framework.test import APIClient

from jornada_milhas.core.models import Destination, Post


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
def photo2():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.seek(0)
    return ContentFile(file.read(), name="photo2.png")


@pytest.fixture
def new_photo():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.seek(0)
    return ContentFile(file.read(), name="new_photo.png")


@pytest.fixture
def new_photo2():
    file = io.BytesIO()
    image = Image.new("RGBA", size=(100, 100), color=(155, 0, 0))
    image.save(file, "png")
    file.seek(0)
    return ContentFile(file.read(), name="new_photo2.png")


@pytest.fixture
def payload_post(user, photo, photo2):
    return {
        "photo": photo,
        "statement": "New",
        "user": user.pk,
    }


@pytest.fixture
def post(request, faker, photo, db):
    m = request.node.get_closest_marker("num_post")
    if m and len(m.args) > 0:
        num_post = m.args[0]
        return baker.make(Post, _quantity=num_post, photo=photo)
    else:
        return baker.make(Post, photo=photo)


@pytest.fixture
def destination(request, faker, photo, photo2, db):
    m = request.node.get_closest_marker("num_destination")
    if m and len(m.args) > 0:
        num_destination = m.args[0]
        return baker.make(Destination, _quantity=num_destination, photo1=photo, photo2=photo2)
    else:
        return baker.make(Destination, photo1=photo, photo2=photo2)


@pytest.fixture
def payload_destination(photo, photo2):
    return {
        "name": "Qualquer lugar",  # TODO: Usar o Fake depois
        "price": "3.10",
        "photo1": photo,
        "photo2": photo2,
        "meta": "meta",
    }
