from django.core.validators import (
    FileExtensionValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models

from .validators import validate_special_characters


class Item(models.Model):
    name = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(2),
            validate_special_characters,
        ],
    )
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.TextField()
    image = models.ImageField(
        upload_to="items",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
    )

    def __str__(self):
        return self.name
