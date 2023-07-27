import pytest

from jornada_milhas.core.serializer import PostSerializer


def test_positive_serializer_one_instance(post):
    serializer = PostSerializer(instance=post)
    data = serializer.data

    assert data["id"] == post.pk
    assert data["statement"] == post.statement
    assert data["user"] == post.user.pk
    assert data["photo"] == post.photo.url


def test_positive_serializer_more_one_instances(posts):
    serializer = PostSerializer(instance=posts, many=True)
    data = serializer.data

    assert len(data) == 5

    for e, d in zip(posts, data):
        assert d["id"] == e.pk
        assert d["statement"] == e.statement
        assert d["user"] == e.user.pk
        assert d["photo"] == e.photo.url


def test_positive_deserializer(payload_post):
    serializer = PostSerializer(data=payload_post)

    assert serializer.is_valid()

    validated = serializer.validated_data

    assert validated["statement"] == payload_post["statement"]
    assert validated["user"].pk == payload_post["user"]
    assert validated["photo"] == payload_post["photo"]


@pytest.mark.parametrize(
    "field,error",
    [
        ("statement", "Este campo é obrigatório."),
        ("user", "Este campo é obrigatório."),
        ("photo", "Nenhum arquivo foi submetido."),
    ],
)
def test_negative_deserializer_missiging_fields(field, error, payload_post):
    data = payload_post.copy()

    del data[field]

    serializer = PostSerializer(data=data)

    assert not serializer.is_valid()

    assert serializer.errors[field] == [error]


@pytest.mark.parametrize(
    "field, value, error",
    [
        ("user", "ab", "Tipo incorreto. Esperado valor pk, recebeu str."),
        ("user", 444, 'Pk inválido "444" - objeto não existe.'),
        ("photo", 1, "O dado submetido não é um arquivo. Certifique-se do tipo de codificação no formulário."),
    ],
    ids=["user-1", "user-2", "photo"],
)
def test_negative_deserializer_error_fields(field, value, error, payload_post):
    data = payload_post.copy()

    data[field] = value

    serializer = PostSerializer(data=data)

    assert not serializer.is_valid()

    assert serializer.errors[field] == [error]
