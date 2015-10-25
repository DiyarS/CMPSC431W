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
                ('primary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BID', models.FloatField()),
                ('reserve_price', models.FloatField()),
                ('expiration_time', models.DateTimeField(verbose_name=b'expiration_date')),
            ],
        ),
        migrations.CreateModel(
            name='Belongs_to',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BID', models.ForeignKey(related_name='bid', to='online_store.Auction')),
                ('item_id', models.ForeignKey(to='online_store.Auction')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('report', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('point_of_contact', models.CharField(max_length=50)),
                ('revenue', models.FloatField()),
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
            name='Fixed_Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Has_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Address')),
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
            name='Individual_buyers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buyer_id', models.CharField(unique=True, max_length=30)),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Individual_sellers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.CharField(unique=True, max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Registered_users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seller_id', models.CharField(unique=True, max_length=30)),
                ('username', models.ForeignKey(to='online_store.Registered_users')),
            ],
        ),
        migrations.AddField(
            model_name='individual_sellers',
            name='seller_id',
            field=models.ForeignKey(related_name='individual_seller_id', to='online_store.Sellers'),
        ),
        migrations.AddField(
            model_name='individual_sellers',
            name='username',
            field=models.ForeignKey(to='online_store.Sellers'),
        ),
        migrations.AddField(
            model_name='individual_buyers',
            name='username',
            field=models.ForeignKey(to='online_store.Registered_users'),
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
            model_name='fixed_price',
            name='item_id',
            field=models.ForeignKey(to='online_store.Items'),
        ),
        migrations.AddField(
            model_name='delivers_to',
            name='buyer_id',
            field=models.ForeignKey(to='online_store.Individual_buyers'),
        ),
        migrations.AddField(
            model_name='delivers_to',
            name='seller_id',
            field=models.ForeignKey(to='online_store.Sellers'),
        ),
        migrations.AddField(
            model_name='companies',
            name='seller_id',
            field=models.ForeignKey(related_name='company_seller_id', to='online_store.Sellers'),
        ),
        migrations.AddField(
            model_name='companies',
            name='username',
            field=models.ForeignKey(to='online_store.Sellers'),
        ),
        migrations.AddField(
            model_name='buys',
            name='item_id',
            field=models.ForeignKey(to='online_store.Fixed_Price'),
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
            field=models.ForeignKey(to='online_store.Items'),
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
        migrations.AddField(
            model_name='auction',
            name='item_id',
            field=models.ForeignKey(to='online_store.Items'),
        ),
    ]
