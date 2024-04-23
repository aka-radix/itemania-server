import random

import factory

from .models import Item


class ItemFactory(factory.Factory):
    """A factory that allows us to create any number of Item instances.

    Images will default to colored squares.
    """

    class Meta:
        model = Item

    name = factory.Faker("license_plate")
    price = factory.Faker("random_int", min=1, max=1000)
    description = factory.Faker("text")
    image = factory.django.ImageField(
        color=factory.LazyFunction(
            lambda: random.choice(["red", "green", "blue"]),
        ),
    )
