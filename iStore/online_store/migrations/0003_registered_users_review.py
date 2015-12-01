# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_auto_20151028_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_users',
            name='review',
            field=models.CharField(default=b'null', max_length=200),
        ),
    ]
