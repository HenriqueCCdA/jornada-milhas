from decimal import Decimal

import pytest

from jornada_milhas.core.serializer import DestinationSerializer


def test_positive_serializer_one_instance(destination):
    serializer = DestinationSerializer(instance=destination)
    data = serializer.data

    assert data["id"] == destination.pk
    assert data["name"] == destination.name
    assert data["price"] == str(destination.price)
    assert data["photo"] == destination.photo.url


def test_positive_serializer_more_one_instances(destinations):
    serializer = DestinationSerializer(instance=destinations, many=True)
    data = serializer.data

    assert len(data) == 6

    for e, d in zip(destinations, data, strict=True):
        assert d["id"] == e.pk
        assert d["name"] == e.name
        assert d["price"] == str(e.price)
        assert d["photo"] == e.photo.url


def test_positive_deserializer(payload_destination):
    serializer = DestinationSerializer(data=payload_destination)

    assert serializer.is_valid()

    validated = serializer.validated_data

    assert validated["name"] == payload_destination["name"]
    assert validated["price"] == Decimal(payload_destination["price"])
    assert validated["photo"] == payload_destination["photo"]


@pytest.mark.parametrize(
    "field,error",
    [
        ("name", "Este campo é obrigatório."),
        ("price", "Este campo é obrigatório."),
        ("photo", "Nenhum arquivo foi submetido."),
    ],
)
def test_negative_deserializer_missiging_fields(field, error, payload_destination):
    data = payload_destination.copy()

    del data[field]

    serializer = DestinationSerializer(data=data)

    assert not serializer.is_valid()

    assert serializer.errors[field] == [error]


@pytest.mark.parametrize(
    "field, value, error",
    [
        ("price", "dd", "Um número válido é necessário."),
        ("price", -1.00, "Certifque-se de que este valor seja maior ou igual a 0.01."),
        ("photo", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["user-1", "user-2", "photo"],
)
def test_negative_deserializer_error_fields(field, value, error, payload_destination):
    data = payload_destination.copy()

    data[field] = value

    serializer = DestinationSerializer(data=data)

    assert not serializer.is_valid()

    assert serializer.errors[field] == [error]
