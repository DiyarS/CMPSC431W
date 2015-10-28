import datetime
from django.utils import timezone

from django.db import models

# Create your models here.

class Items(models.Model):
	item_id = models.CharField(max_length=30, unique=True, primary_key=True )
	description = models.CharField(max_length=500)
	location = models.CharField(max_length=60)
	rating = models.FloatField()



class  Category(models.Model):
    name = models.CharField(max_length=60, unique=True, primary_key=True)
    report = models.TextField(max_length=1000)


class  Fixed_Price(models.Model):
    item_id = models.ForeignKey(Items, unique=True, primary_key=True)
    price = models.FloatField()


class  Auction(models.Model):
    item_id = models.ForeignKey(Items, unique=True, primary_key=True)
    BID = models.FloatField() 
    reserve_price = models.FloatField()
    expiration_time = models.DateTimeField()


class  Belongs_to(models.Model):
    category = models.CharField(max_length=30, unique=True, primary_key=True)
    item_id = models.ForeignKey(Items, unique=True) 
    subcategory = models.ForeignKey(Category, related_name = 'subcategory')
    parent_category = models.ForeignKey(Category, related_name = 'parent_category')
    


class  Registered_users(models.Model):
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)

class  Sellers(models.Model):
    username = models.ForeignKey(Registered_users, primary_key=True)
    seller_id = models.CharField(max_length=30, unique=True)


class  Companies(models.Model):
    username = models.ForeignKey(Sellers, to_field='username_id', default='null', primary_key=True)
    seller_id = models.ForeignKey(Sellers, to_field='seller_id', related_name='seller_id_id', default='-1')
    name = models.CharField(max_length=30)
    point_of_contact = models.CharField(max_length=50)
    revenue = models.FloatField()


class  Individual_sellers(models.Model):
    username = models.ForeignKey(Sellers, to_field='username_id', default='null', primary_key=True)
    seller_id = models.ForeignKey(Sellers, to_field='seller_id', related_name = 'individual_seller_id')
    dob = models.DateField('date_of_birth')
    gender = models.CharField(max_length=10)
    annual_income = models.FloatField()

class  Individual_buyers(models.Model):
    username = models.ForeignKey(Registered_users, primary_key=True)
    buyer_id = models.CharField(max_length=30, unique=True)
    dob = models.DateField('date_of_birth')
    gender = models.CharField(max_length=10)
    annual_income = models.FloatField()

class Address(models.Model):
	street = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 30)
	index = models.CharField(max_length = 20)
	primary = models.IntegerField(unique=True)

class  Delivers_to(models.Model):
    seller_id = models.ForeignKey(Sellers, to_field='seller_id', default='null')
    buyer_id = models.ForeignKey(Individual_buyers, to_field='buyer_id', default='null')
    address = models.ForeignKey(Address)
    payment_confirmation = models.BooleanField()


class Has_address(models.Model):
	username = models.ForeignKey(Registered_users)
	primary = models.ForeignKey(Address, to_field='primary')

class Credit_card(models.Model):
	card_number = models.CharField(max_length=20, unique=True)
	name_on_card = models.CharField(max_length=40)
	expiration_date = models.DateField('expiration_date')
	code = models.CharField(max_length=4)
	primary = models.IntegerField()

class Has_credit_card(models.Model):
	username = models.ForeignKey(Registered_users)
	primary = models.ForeignKey(Credit_card)


class Bids(models.Model):
	item_id = models.ForeignKey(Auction)
	BID = models.FloatField()
	username = models.ForeignKey(Registered_users)

class Buys(models.Model):
	item_id = models.ForeignKey(Fixed_Price)
	username = models.ForeignKey(Registered_users)

