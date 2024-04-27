import re

from django.core.exceptions import ValidationError


def validate_special_characters(value):
    """Validate special characters in name."""

    if not re.match(r"^[a-zA-Z0-9\s]+$", value):
        raise ValidationError(
            "Special characters are not allowed",
            params={"value": value},
        )
