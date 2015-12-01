# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='auction',
            options={'verbose_name_plural': 'Auctions'},
        ),
        migrations.AlterModelOptions(
            name='belongs_to',
            options={'verbose_name_plural': 'Belongs_to'},
        ),
        migrations.AlterModelOptions(
            name='bids',
            options={'verbose_name_plural': 'Bids'},
        ),
        migrations.AlterModelOptions(
            name='buys',
            options={'verbose_name_plural': 'Buys'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='credit_card',
            options={'verbose_name_plural': 'Credit_cards'},
        ),
        migrations.AlterModelOptions(
            name='delivers_to',
            options={'verbose_name_plural': 'Delivers_to'},
        ),
        migrations.AlterModelOptions(
            name='fixed_price',
            options={'verbose_name_plural': 'Fixed_Prices'},
        ),
        migrations.AlterModelOptions(
            name='has_address',
            options={'verbose_name_plural': 'Has_addresses'},
        ),
        migrations.AlterModelOptions(
            name='has_credit_card',
            options={'verbose_name_plural': 'Has_credit_cards'},
        ),
        migrations.AlterModelOptions(
            name='individual_buyers',
            options={'verbose_name_plural': 'Individual_buyers'},
        ),
        migrations.AlterModelOptions(
            name='individual_sellers',
            options={'verbose_name_plural': 'Individual_sellers'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='registered_users',
            options={'verbose_name_plural': 'Registered_users'},
        ),
        migrations.AlterModelOptions(
            name='sellers',
            options={'verbose_name_plural': 'Sellers'},
        ),
    ]
