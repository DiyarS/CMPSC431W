import django
import os
from iStore import *

os.environ['DJANGO_SETTINGS_MODULE']='iStore.settings'
django.setup()

from online_store.models import Items, Category, Fixed_Price, Auction, Belongs_to, Registered_users, Sellers, Companies, Individual_sellers, Individual_buyers, Address, Credit_card, Has_address, Has_credit_card, Bids


#read a list of items and store it in the Items database
with open('items_input.txt', mode='r') as myfile:
	items = myfile.readlines()
	for item in items:
		item_as_dict = eval(item)
		i = Items(item_id = item_as_dict['item_id'], description = item_as_dict['description'], location = item_as_dict['location'], rating = item_as_dict['rating'])
		i.save()

myfile.close()