# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_registered_users_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belongs_to',
            name='item_id',
            field=models.ForeignKey(to='online_store.Items'),
        ),
    ]
