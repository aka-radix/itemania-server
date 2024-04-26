from django.core.management.base import BaseCommand

from itemania.items.model_factories import ItemFactory
from itemania.items.models import Item


class Command(BaseCommand):
    help = "Generate fake items"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=10,
            help="Number of items to generate",
        )

    def handle(self, *args, **options):  # noqa: ARG002
        count = int(options["number"])
        Item.objects.bulk_create(ItemFactory.create_batch(count))
        self.stdout.write(
            self.style.SUCCESS(f"{count} items generated successfully!"),
        )
