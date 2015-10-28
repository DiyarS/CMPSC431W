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
        ),
        migrations.CreateModel(
            name='Belongs_to',
            fields=[
                ('category', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BID', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Buys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=60, unique=True, serialize=False, primary_key=True)),
                ('report', models.TextField(max_length=1000)),
            ],
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
        ),
        migrations.CreateModel(
            name='Delivers_to',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_confirmation', models.BooleanField()),
                ('address', models.ForeignKey(to='online_store.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Has_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Address', to_field=b'primary')),
            ],
        ),
        migrations.CreateModel(
            name='Has_credit_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Credit_card')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Registered_users',
            fields=[
                ('username', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('BID', models.FloatField()),
                ('reserve_price', models.FloatField()),
                ('expiration_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Fixed_Price',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('price', models.FloatField()),
            ],
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
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Registered_users')),
                ('seller_id', models.CharField(unique=True, max_length=30)),
            ],
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
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'null', to_field=b'username_id', serialize=False, to='online_store.Sellers')),
                ('name', models.CharField(max_length=30)),
                ('point_of_contact', models.CharField(max_length=50)),
                ('revenue', models.FloatField()),
            ],
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
