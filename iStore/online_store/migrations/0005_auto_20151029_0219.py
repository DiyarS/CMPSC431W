# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0004_auto_20151029_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='belongs_to',
            name='parent_category',
        ),
        migrations.RemoveField(
            model_name='belongs_to',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_cat',
            field=models.ForeignKey(related_name='parent_category', to='online_store.Category', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='subcat',
            field=models.ForeignKey(related_name='subcategory', to='online_store.Category', null=True),
        ),
    ]
