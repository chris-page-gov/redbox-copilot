import json
import logging
from http import HTTPStatus

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from redbox_app.redbox_core.models import ChatMessage

User = get_user_model()

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
def test_post_new_rating_only(alice: User, chat_message: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message.id})
    response = client.post(url, json.dumps({"rating": 5, "text": ""}), content_type="application/json")

    # Then
    status = HTTPStatus(response.status_code)
    assert status.is_success
    chat_message.refresh_from_db()
    assert chat_message.rating == 5
    assert chat_message.rating_text == ""
    assert chat_message.rating_chips == []


@pytest.mark.django_db()
def test_post_new_rating(alice: User, chat_message: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message.id})
    response = client.post(
        url,
        json.dumps({"rating": 5, "text": "Lorem Ipsum.", "chips": ["speed", "accuracy", "swearing"]}),
        content_type="application/json",
    )

    # Then
    status = HTTPStatus(response.status_code)
    assert status.is_success
    chat_message.refresh_from_db()
    assert chat_message.rating == 5
    assert chat_message.rating_text == "Lorem Ipsum."
    assert set(chat_message.rating_chips) == {"speed", "accuracy", "swearing"}


@pytest.mark.django_db()
def test_post_invalid_rating(alice: User, chat_message: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message.id})
    response = client.post(
        url,
        json.dumps({"rating": 3.4, "text": [42], "chips": {"speed": "accuracy"}}),
        content_type="application/json",
    )

    # Then
    status = HTTPStatus(response.status_code)
    assert not status.is_success
    chat_message.refresh_from_db()
    assert response.json() == {
        "chips": ['Expected a list of items but got type "dict".'],
        "rating": ["A valid integer is required."],
        "text": ["Not a valid string."],
    }


@pytest.mark.django_db()
def test_post_new_rating_with_naughty_string(alice: User, chat_message: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message.id})
    response = client.post(
        url,
        json.dumps({"rating": 5, "text": "Lorem Ipsum. \x00", "chips": ["speed", "accuracy", "swearing"]}),
        content_type="application/json",
    )

    # Then
    status = HTTPStatus(response.status_code)
    assert status.is_success
    chat_message.refresh_from_db()
    assert chat_message.rating == 5
    assert chat_message.rating_text == "Lorem Ipsum. \ufffd"
    assert set(chat_message.rating_chips) == {"speed", "accuracy", "swearing"}


@pytest.mark.django_db()
def test_post_updated_rating(alice: User, chat_message_with_rating: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message_with_rating.id})
    response = client.post(
        url,
        json.dumps({"rating": 5, "text": "Lorem Ipsum.", "chips": ["speed", "accuracy", "swearing"]}),
        content_type="application/json",
    )

    # Then
    status = HTTPStatus(response.status_code)
    assert status.is_success
    chat_message_with_rating.refresh_from_db()
    assert chat_message_with_rating.rating == 5
    assert chat_message_with_rating.rating_text == "Lorem Ipsum."
    assert set(chat_message_with_rating.rating_chips) == {"speed", "accuracy", "swearing"}


@pytest.mark.django_db()
def test_post_updated_rating_with_naughty_string(alice: User, chat_message_with_rating: ChatMessage, client: Client):
    # Given
    client.force_login(alice)

    # When
    url = reverse("ratings", kwargs={"message_id": chat_message_with_rating.id})
    response = client.post(
        url,
        json.dumps({"rating": 5, "text": "Lorem Ipsum. \x00", "chips": ["speed", "accuracy", "swearing"]}),
        content_type="application/json",
    )

    # Then
    status = HTTPStatus(response.status_code)
    assert status.is_success
    chat_message_with_rating.refresh_from_db()
    assert chat_message_with_rating.rating == 5
    assert chat_message_with_rating.rating_text == "Lorem Ipsum. \ufffd"
    assert set(chat_message_with_rating.rating_chips) == {"speed", "accuracy", "swearing"}
