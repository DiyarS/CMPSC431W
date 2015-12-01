# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'email address', db_index=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=30)),
                ('review', models.CharField(default=b'null', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='bids',
            name='username',
            field=models.ForeignKey(to='online_store.User'),
        ),
        migrations.AlterField(
            model_name='buys',
            name='username',
            field=models.ForeignKey(to='online_store.User'),
        ),
        migrations.AlterField(
            model_name='has_address',
            name='username',
            field=models.ForeignKey(to='online_store.User'),
        ),
        migrations.AlterField(
            model_name='has_credit_card',
            name='username',
            field=models.ForeignKey(to='online_store.User'),
        ),
        migrations.AlterField(
            model_name='individual_buyers',
            name='username',
            field=models.ForeignKey(primary_key=True, serialize=False, to='online_store.User'),
        ),
        migrations.AlterField(
            model_name='sellers',
            name='username',
            field=models.ForeignKey(primary_key=True, serialize=False, to='online_store.User'),
        ),
        migrations.DeleteModel(
            name='Registered_users',
        ),
    ]
