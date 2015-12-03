# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_items_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
