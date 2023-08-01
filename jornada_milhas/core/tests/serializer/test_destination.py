from decimal import Decimal

import pytest

from jornada_milhas.core.serializer import DestinationSerializer


def test_positive_serializer_one_instance(destination):
    serializer = DestinationSerializer(instance=destination)
    data = serializer.data

    assert data["id"] == destination.pk
    assert data["name"] == destination.name
    assert data["price"] == str(destination.price)
    assert data["photo1"] == destination.photo1.url
    assert data["photo2"] == destination.photo2.url
    assert data["meta"] == destination.meta
    assert data["describe"] is None


def test_positive_serializer_more_one_instances(destinations):
    serializer = DestinationSerializer(instance=destinations, many=True)
    data = serializer.data

    assert len(data) == 6

    for e, d in zip(destinations, data, strict=True):
        assert d["id"] == e.pk
        assert d["name"] == e.name
        assert d["price"] == str(e.price)
        assert d["photo1"] == e.photo1.url
        assert d["photo2"] == e.photo2.url
        assert d["meta"] == e.meta
        assert d["describe"] is None


def test_positive_deserializer(payload_destination):
    serializer = DestinationSerializer(data=payload_destination)

    assert serializer.is_valid()

    validated = serializer.validated_data

    assert validated["name"] == payload_destination["name"]
    assert validated["price"] == Decimal(payload_destination["price"])
    assert validated["photo1"] == payload_destination["photo1"]


@pytest.mark.parametrize(
    "field,error",
    [
        ("name", "Este campo é obrigatório."),
        ("price", "Este campo é obrigatório."),
        ("photo1", "Nenhum arquivo foi submetido."),
        ("photo2", "Nenhum arquivo foi submetido."),
        ("meta", "Este campo é obrigatório."),
    ],
    ids=["name", "price", "photo1", "photo2", "meta"],
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
        ("photo1", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
        ("photo2", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["price-1", "price-2", "photo1", "photo2"],
)
def test_negative_deserializer_error_fields(field, value, error, payload_destination):
    data = payload_destination.copy()

    data[field] = value

    serializer = DestinationSerializer(data=data)

    assert not serializer.is_valid()

    assert serializer.errors[field] == [error]
