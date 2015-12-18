# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.', verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name=b'active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined')),
                ('phone_number', models.CharField(max_length=30)),
                ('review', models.CharField(default=b'null', max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
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
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BID', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Bids',
            },
        ),
        migrations.CreateModel(
            name='Buys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Buys',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=60, unique=True, serialize=False, primary_key=True)),
                ('report', models.TextField(max_length=1000)),
                ('parent_cat', models.ForeignKey(related_name='parent_category', to='online_store.Category', null=True)),
                ('subcategory', models.ForeignKey(to='online_store.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
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
            options={
                'verbose_name_plural': 'Credit_cards',
            },
        ),
        migrations.CreateModel(
            name='Delivers_to',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_confirmation', models.BooleanField()),
                ('address', models.ForeignKey(to='online_store.Address')),
            ],
            options={
                'verbose_name_plural': 'Delivers_to',
            },
        ),
        migrations.CreateModel(
            name='Has_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Address', to_field=b'primary')),
            ],
            options={
                'verbose_name_plural': 'Has_addresses',
            },
        ),
        migrations.CreateModel(
            name='Has_credit_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.ForeignKey(to='online_store.Credit_card')),
            ],
            options={
                'verbose_name_plural': 'Has_credit_cards',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=60)),
                ('rating', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('BID', models.FloatField()),
                ('reserve_price', models.FloatField()),
                ('expiration_time', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Auctions',
            },
        ),
        migrations.CreateModel(
            name='Belongs_to',
            fields=[
                ('category', models.CharField(max_length=30)),
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items')),
            ],
            options={
                'verbose_name_plural': 'Belongs_to',
            },
        ),
        migrations.CreateModel(
            name='Fixed_Price',
            fields=[
                ('item_id', models.ForeignKey(primary_key=True, serialize=False, to='online_store.Items', unique=True)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Fixed_Prices',
            },
        ),
        migrations.CreateModel(
            name='Individual_buyers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('buyer_id', models.CharField(unique=True, max_length=30)),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Individual_buyers',
            },
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'user', serialize=False, to=settings.AUTH_USER_MODEL, unique=True)),
                ('seller_id', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Sellers',
            },
        ),
        migrations.AddField(
            model_name='has_credit_card',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='has_address',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buys',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bids',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'null', to_field=b'username_id', serialize=False, to='online_store.Sellers')),
                ('name', models.CharField(max_length=30)),
                ('point_of_contact', models.CharField(max_length=50)),
                ('revenue', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Individual_sellers',
            fields=[
                ('username', models.ForeignKey(primary_key=True, default=b'null', to_field=b'username_id', serialize=False, to='online_store.Sellers')),
                ('dob', models.DateField(verbose_name=b'date_of_birth')),
                ('gender', models.CharField(max_length=10)),
                ('annual_income', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Individual_sellers',
            },
        ),
        migrations.AddField(
            model_name='sellers',
            name='item_id',
            field=models.ForeignKey(to='online_store.Items', null=True),
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
            model_name='individual_sellers',
            name='seller_id',
            field=models.ForeignKey(related_name='individual_seller_id', to='online_store.Sellers', to_field=b'seller_id'),
        ),
        migrations.AddField(
            model_name='companies',
            name='seller_id',
            field=models.ForeignKey(related_name='seller_id_id', default=b'-1', to_field=b'seller_id', to='online_store.Sellers'),
        ),
    ]
