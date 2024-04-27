from django.apps import AppConfig


class ItemsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "itemania.items"

    def ready(self):
        from .model_factories import ItemFactory
        from .models import Item

        if not Item.objects.exists():
            Item.objects.bulk_create(ItemFactory.create_batch(10))
