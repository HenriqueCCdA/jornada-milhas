from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist
from faker import Faker
from model_bakery import baker

User = get_user_model()
fake = Faker()


@pytest.fixture
def user(db):
    return baker.make(User)


@pytest.fixture
def superuser(db):
    return User.objects.create_superuser(email=fake.email(), password=fake.password())


def test_positive_create(user):
    assert user.pk
    assert User.objects.exists()


def test_positive_create_superuser(superuser):
    assert superuser.is_staff
    assert superuser.is_superuser


def test_positive_default(user):
    assert not user.is_staff
    assert user.is_active


def test_create_at_and_modified_at(user):
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.modified_at, datetime)


def test_str(user):
    assert str(user) == user.email


def test_fields():
    # TODO: Será que tem alguma forma melhor de testar o fields?
    try:
        User._meta.get_field("name")
        User._meta.get_field("email")
        User._meta.get_field("is_staff")
        User._meta.get_field("is_active")
        User._meta.get_field("password")
        User._meta.get_field("last_login")
    except FieldDoesNotExist as e:
        assert False, str(e)
