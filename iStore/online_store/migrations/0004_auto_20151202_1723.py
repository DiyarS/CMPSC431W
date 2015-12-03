# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_auto_20151202_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belongs_to',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='belongs_to',
            name='item_id',
            field=models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items'),
        ),
    ]
