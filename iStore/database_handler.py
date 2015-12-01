import django
import os
from iStore import *

os.environ['DJANGO_SETTINGS_MODULE']='iStore.settings'
django.setup()

<<<<<<< HEAD
from online_store.models import Items, Category, Fixed_Price, Auction, Belongs_to, User, Sellers, Companies, Individual_sellers, Individual_buyers, Address, Credit_card, Has_address, Has_credit_card, Bids


=======
from online_store.models import Items, Category, Fixed_Price, Auction, Belongs_to, Registered_users, Sellers, Companies, Individual_sellers, Individual_buyers, Address, Credit_card, Has_address, Has_credit_card, Bids

if __name__ == '__main__':
    populate_categories_database()
    populate_items_database()
    populate_registered_users_database()
    build_categories_hierarchy()
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6


def populate_categories_database():
	#read a list of categories and store it in the Category database
	with open('categories_input.txt', mode='r') as myfile:
		categories = myfile.readlines()
		for category in categories:
			category_as_dict = eval(category)
			c = Category(name = category_as_dict['name'], report = category_as_dict['report'])
			c.save()

	myfile.close()


def populate_items_database():
	#read a list of items and store it in the Items database
	with open('items_input.txt', mode='r') as myfile:
		items = myfile.readlines()
		for item in items:
			item_as_dict = eval(item)
			i = Items(item_id = item_as_dict['item_id'], description = item_as_dict['description'], location = item_as_dict['location'], rating = item_as_dict['rating'])
			i.save()

	myfile.close()



def populate_registered_users_database():
	#read a list of users and store it in the Registered_users database
	with open('users_input.txt', mode='r') as myfile:
		users = myfile.readlines()
		for user in users:
			user_as_dict = eval(user)
<<<<<<< HEAD
			u = User(password = user_as_dict['password'], phone_number = user_as_dict['phone_number'], email = user_as_dict['email'], review = user_as_dict['review'])
=======
			u = Registered_users(username = user_as_dict['username'], password = user_as_dict['password'], phone_number = user_as_dict['phone_number'], email = user_as_dict['email'], review = user_as_dict['review'])
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6
			u.save()

	myfile.close()


#create a hierarchy of categories
def build_categories_hierarchy():
	all_items_category = Category.objects.get(name="All items")
	
	books_category = Category.objects.get(name="Books")
	audio_books_category = Category.objects.get(name="Audio books")
	kindle_books_category = Category.objects.get(name="Kindle books")
	long_reads_category = Category.objects.get(name="Long reads")
	short_reads_category = Category.objects.get(name="Short reads")
	
	clothing_and_shoes_category = Category.objects.get(name="Clothing & Shoes")
	men_category = Category.objects.get(name="Men")
	women_category = Category.objects.get(name="Women")
	clothing_category = Category.objects.get(name="Clothing")
	shoes_category = Category.objects.get(name="Shoes")
	

	electronics_and_computers_category = Category.objects.get(name="Electronics & Computers")
	
	computers_category = Category.objects.get(name="Computers")
	laptops_category = Category.objects.get(name="Laptops")
	macbooks_category = Category.objects.get(name="Macbooks")
	samsung_laptops_category = Category.objects.get(name="Samsung laptops")
	dell_category = Category.objects.get(name="Dell")
	lenovo_category = Category.objects.get(name="Lenovo")
	
	desktop_computers_category = Category.objects.get(name="Desktop computers")
	
	tvs_category = Category.objects.get(name="TVs")
	samsung_tvs_category = Category.objects.get(name="Samsung TVs")
	lg_tvs_category = Category.objects.get(name="LG TVs")
	

	random_item = Items.objects.get(item_id=0) 
	

	all_items_category = Category(name=all_items_category.name, report=all_items_category.report, subcategory = books_category, parent_cat = all_items_category)
	books_category = Category(name=books_category.name, report=books_category.report, subcategory = audio_books_category, parent_cat = all_items_category)
	audio_books_category = Category(name=audio_books_category.name, report=audio_books_category.report, subcategory = short_reads_category, parent_cat = books_category)
	kindle_books_category = Category(name=kindle_books_category.name, report=kindle_books_category.report, subcategory = short_reads_category, parent_cat = books_category)
	short_reads_category = Category(name=short_reads_category.name, report=short_reads_category.report, subcategory = None, parent_cat = audio_books_category)
	long_reads_category = Category(name=long_reads_category.name, report=long_reads_category.report, subcategory = None, parent_cat = audio_books_category)
	
	clothing_and_shoes_category = Category(name=clothing_and_shoes_category.name, report=clothing_and_shoes_category.report, subcategory = clothing_category, parent_cat = all_items_category)
	men_category = Category(name=men_category.name, report=men_category.report, subcategory = clothing_category, parent_cat = clothing_and_shoes_category)
	women_category = Category(name=women_category.name, report=women_category.report, subcategory = clothing_category, parent_cat = clothing_and_shoes_category)
	clothing_category = Category(name=clothing_category.name, report=clothing_category.report, subcategory = None, parent_cat = men_category)
	shoes_category = Category(name=shoes_category.name, report=shoes_category.report, subcategory = None, parent_cat = men_category)

	electronics_and_computers_category = Category(name=electronics_and_computers_category.name, report=electronics_and_computers_category.report, subcategory = computers_category, parent_cat = all_items_category)
	computers_category = Category(name=computers_category.name, report=computers_category.report, subcategory = macbooks_category, parent_cat = electronics_and_computers_category)
	macbooks_category = Category(name=macbooks_category.name, report=macbooks_category.report, subcategory = None, parent_cat = computers_category)
	dell_category = Category(name=dell_category.name, report=dell_category.report, subcategory = None, parent_cat = computers_category)
	samsung_laptops_category = Category(name=samsung_laptops_category.name, report=samsung_laptops_category.report, subcategory = None, parent_cat = computers_category)
	lenovo_category = Category(name=lenovo_category.name, report=lenovo_category.report, subcategory = None, parent_cat = computers_category)
	desktop_computers_category = Category(name=desktop_computers_category.name, report=desktop_computers_category.report, subcategory = None, parent_cat = computers_category)
	
	tvs_category = Category(name=tvs_category.name, report=tvs_category.report, subcategory = samsung_tvs_category, parent_cat = electronics_and_computers_category)
	samsung_tvs_category = Category(name=samsung_tvs_category.name, report=samsung_tvs_category.report, subcategory = None, parent_cat = tvs_category)
	lg_tvs_category = Category(name=lg_tvs_category.name, report=lg_tvs_category.report, subcategory = None, parent_cat = tvs_category)
	





	
	
	#all_items_hierarchy = Belongs_to(category = all_items_category.name, item_id = random_item, subcategory = books_category, parent_category = all_items_category)
	#books_hierarchy = Belongs_to(category = books_category.name, item_id = random_item, subcategory = audio_books_category, parent_category = all_items_category)
	#kindle_books_hierarchy = Belongs_to(category = kindle_books_category.name, item_id = random_item, subcategory = long_reads_books_category, parent_category = books_category)
	#books_hierarchy = Belongs_to(category = books_category.name, item_id = random_item, subcategory = audio_books_category, parent_category = all_items_category)


<<<<<<< HEAD
if __name__ == '__main__':
    populate_categories_database()
    populate_items_database()
    populate_registered_users_database()
    build_categories_hierarchy()

=======
>>>>>>> 0a473c6cb19413833ef8cd13785ad8724fc7efb6




