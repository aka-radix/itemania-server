from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="items", blank=True, null=True)

    def __str__(self):
        return self.name
