# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0005_auto_20151029_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcat',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(to='online_store.Category', null=True),
        ),
    ]
