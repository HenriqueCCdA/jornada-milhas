from datetime import datetime

from django.core.exceptions import FieldDoesNotExist

from jornada_milhas.core.models import Post


def test_positive_create(post):
    assert post.pk
    assert Post.objects.exists()


def test_create_at_and_modified_at(post):
    assert isinstance(post.created_at, datetime)
    assert isinstance(post.modified_at, datetime)


def test_str(post):
    assert str(post) == f"{post.pk} - {post.user.name}"


def test_fields():
    # TODO: Será que tem alguma forma melhor de testar o fields?
    try:
        Post._meta.get_field("user")
        Post._meta.get_field("photo")
        Post._meta.get_field("statement")
    except FieldDoesNotExist as e:
        assert False, str(e)
