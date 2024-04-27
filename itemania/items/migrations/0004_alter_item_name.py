# Generated by Django 5.0.4 on 2024-04-27 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
