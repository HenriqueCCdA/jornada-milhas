from datetime import datetime
from decimal import Decimal

from django.core.exceptions import FieldDoesNotExist
from django.core.validators import MinValueValidator

from jornada_milhas.core.models import Destination


def test_positive_create(destination):
    assert destination.pk
    assert Destination.objects.exists()


def test_create_at_and_modified_at(destination):
    assert isinstance(destination.created_at, datetime)
    assert isinstance(destination.modified_at, datetime)


def test_str(destination):
    assert str(destination) == destination.name


def test_fields():
    # TODO: Será que tem alguma forma melhor de testar o fields?
    try:
        Destination._meta.get_field("name")
        Destination._meta.get_field("photo1")
        Destination._meta.get_field("photo2")
        Destination._meta.get_field("price")
        Destination._meta.get_field("meta")
        Destination._meta.get_field("describe")
    except FieldDoesNotExist as e:
        raise AssertionError(e) from e


def test_metadata():
    assert Destination._meta.get_field("name").max_length == 200

    assert Destination._meta.get_field("meta").max_length == 160

    assert Destination._meta.get_field("describe").blank

    assert Destination._meta.get_field("price").max_digits == 14
    assert Destination._meta.get_field("price").decimal_places == 2
    assert MinValueValidator(Decimal("0.01")) in Destination._meta.get_field("price").validators
