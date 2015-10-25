import datetime
from django.utils import timezone

from django.db import models

# Create your models here.

class Items(models.Model):
	item_id = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=500)
	location = models.CharField(max_length=60)
	rating = models.FloatField()

class  Fixed_Price(models.Model):
    item_id = models.ForeignKey(Items)
    price = models.FloatField()
    

class  Auction(models.Model):
    item_id = models.ForeignKey(Items)
    BID = models.FloatField() 
    reserve_price = models.FloatField()
    expiration_time = models.DateTimeField('expiration_date')

class  Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    report = models.TextField(max_length=1000)


class  Belongs_to(models.Model):
    item_id = models.ForeignKey(Items)
    subcategory = models.ForeignKey(Category, related_name = 'subcategory')
    parent_category = models.ForeignKey(Category, related_name = 'parent_category')
    category = models.CharField(max_length=30, unique=True)

class  Registered_users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)

class  Sellers(models.Model):
    username = models.ForeignKey(Registered_users)
    seller_id = models.CharField(max_length=30, unique=True)

class  Companies(models.Model):
    username = models.ForeignKey(Sellers)
    seller_id = models.ForeignKey(Sellers, related_name='company_seller_id')
    name = models.CharField(max_length=30)
    point_of_contact = models.CharField(max_length=50)
    revenue = models.FloatField()

class  Individual_sellers(models.Model):
    username = models.ForeignKey(Sellers)
    seller_id = models.ForeignKey(Sellers, related_name = 'individual_seller_id')
    dob = models.DateField('date_of_birth')
    gender = models.CharField(max_length=10)
    annual_income = models.FloatField()

class  Individual_buyers(models.Model):
    username = models.ForeignKey(Registered_users)
    buyer_id = models.CharField(max_length=30, unique=True)
    dob = models.DateField('date_of_birth')
    gender = models.CharField(max_length=10)
    annual_income = models.FloatField()

class Address(models.Model):
	street = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 30)
	index = models.CharField(max_length = 20)
	primary = models.IntegerField()

class  Delivers_to(models.Model):
    seller_id = models.ForeignKey(Sellers)
    buyer_id = models.ForeignKey(Individual_buyers)
    address = models.ForeignKey(Address)
    payment_confirmation = models.BooleanField()


class Has_address(models.Model):
	username = models.ForeignKey(Registered_users)
	primary = models.ForeignKey(Address)

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
	BID = models.ForeignKey(Auction, related_name = 'bid')
	username = models.ForeignKey(Registered_users)

class Buys(models.Model):
	item_id = models.ForeignKey(Fixed_Price)
	username = models.ForeignKey(Registered_users)




