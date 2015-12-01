# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('index', models.CharField(max_length=20)),
                ('primary', models.IntegerField(unique=True)),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Addresses',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Belongs_to',
            fields=[
                ('category', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Belongs_to',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BID', models.FloatField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Bids',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Buys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Buys',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=60, unique=True, serialize=False, primary_key=True)),
                ('report', models.TextField(max_length=1000)),
<<<<<<< HEAD
                ('parent_cat', models.ForeignKey(related_name='parent_category', to='online_store.Category', null=True)),
                ('subcategory', models.ForeignKey(to='online_store.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
=======
            ],
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Credit_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_number', models.CharField(unique=True, max_length=20)),
                ('name_on_card', models.CharField(max_length=40)),
                ('expiration_date', models.DateField(verbose_name=b'expiration_date')),
                ('code', models.CharField(max_length=4)),
                ('primary', models.IntegerField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Credit_cards',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Delivers_to',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_confirmation', models.BooleanField()),
                ('address', models.ForeignKey(to='online_store.Address')),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Delivers_to',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Has_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Address', to_field=b'primary')),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Has_addresses',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Has_credit_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Credit_card')),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Has_credit_cards',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Items',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Registered_users',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=30)),
                ('review', models.CharField(default=b'null', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Registered_users',
            },
=======
                ('username', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=30)),
            ],
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('BID', models.FloatField()),
                ('reserve_price', models.FloatField()),
                ('expiration_time', models.DateTimeField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Auctions',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Fixed_Price',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('price', models.FloatField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Fixed_Prices',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Individual_buyers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Registered_users')),
                ('buyer_id', models.CharField(unique=True, max_length=30)),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Individual_buyers',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Registered_users')),
                ('seller_id', models.CharField(unique=True, max_length=30)),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Sellers',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.AddField(
            model_name='has_credit_card',
            name='username',
            field=models.ForeignKey(to='online_store.Registered_users'),
        ),
        migrations.AddField(
            model_name='has_address',
            name='username',
            field=models.ForeignKey(to='online_store.Registered_users'),
        ),
        migrations.AddField(
            model_name='buys',
            name='username',
            field=models.ForeignKey(to='online_store.Registered_users'),
        ),
        migrations.AddField(
            model_name='bids',
            name='username',
            field=models.ForeignKey(to='online_store.Registered_users'),
        ),
        migrations.AddField(
            model_name='belongs_to',
            name='item_id',
<<<<<<< HEAD
            field=models.ForeignKey(to='online_store.Items'),
=======
            field=models.ForeignKey(to='online_store.Items', unique=True),
        ),
        migrations.AddField(
            model_name='belongs_to',
            name='parent_category',
            field=models.ForeignKey(related_name='parent_category', to='online_store.Category'),
        ),
        migrations.AddField(
            model_name='belongs_to',
            name='subcategory',
            field=models.ForeignKey(related_name='subcategory', to='online_store.Category'),
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'null', to_field=b'username_id', serialize=False, to='online_store.Sellers')),
                ('name', models.CharField(max_length=30)),
                ('point_of_contact', models.CharField(max_length=50)),
                ('revenue', models.FloatField()),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Companies',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.CreateModel(
            name='Individual_sellers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'null', to_field=b'username_id', serialize=False, to='online_store.Sellers')),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
                ('seller_id', models.ForeignKey(related_name='individual_seller_id', to='online_store.Sellers', to_field=b'seller_id')),
            ],
<<<<<<< HEAD
            options={
                'verbose_name_plural': 'Individual_sellers',
            },
=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
        ),
        migrations.AddField(
            model_name='delivers_to',
            name='buyer_id',
            field=models.ForeignKey(to='online_store.Individual_buyers', default=b'null', to_field=b'buyer_id'),
        ),
        migrations.AddField(
            model_name='delivers_to',
            name='seller_id',
            field=models.ForeignKey(to='online_store.Sellers', default=b'null', to_field=b'seller_id'),
        ),
        migrations.AddField(
            model_name='buys',
            name='item_id',
            field=models.ForeignKey(to='online_store.Fixed_Price'),
        ),
        migrations.AddField(
            model_name='bids',
            name='item_id',
            field=models.ForeignKey(to='online_store.Auction'),
        ),
        migrations.AddField(
            model_name='companies',
            name='seller_id',
            field=models.ForeignKey(related_name='seller_id_id', default=b'-1', to_field=b'seller_id', to='online_store.Sellers'),
        ),
    ]
