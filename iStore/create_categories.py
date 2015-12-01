categories = []

categories.append({'name':"All items", 'report': "Periodic reports"})

for x in range(1, 22):
	categories.append({'name': "", 'report': "Periodic reports"})

#create category names
books_category1 = "Books"
books_category2 = "Audio books"
books_category3 = "Kindle books"
books_category4 = "Short reads"
books_category5 = "Long reads"

categories[1]["name"] = books_category1
categories[2]["name"] = books_category2
categories[3]["name"] = books_category3
categories[4]["name"] = books_category4
categories[5]["name"] = books_category5

electronics_category1 = "Electronics & Computers"
electronics_category2 = "TVs"
electronics_category3 = "Samsung TVs"
electronics_category4 = "LG TVs"
electronics_category5 = "Computers"
electronics_category6 = "Laptops"
electronics_category7 = "Desktop computers"
electronics_category8 = "Macbooks"
electronics_category9 = "Samsung laptops"
electronics_category10 = "Dell"
electronics_category11 = "Lenovo"

categories[6]["name"] = electronics_category1
categories[7]["name"] = electronics_category2
categories[8]["name"] = electronics_category3
categories[9]["name"] = electronics_category4
categories[10]["name"] = electronics_category5
categories[11]["name"] = electronics_category6
categories[12]["name"] = electronics_category7
categories[13]["name"] = electronics_category8
categories[14]["name"] = electronics_category9
categories[15]["name"] = electronics_category10
categories[16]["name"] = electronics_category11


#create clothing categories and add to the array of categories
clothing_category1 = "Clothing & Shoes"
clothing_category2 = "Men"
clothing_category3 = "Women"
clothing_category4 = "Clothing"
clothing_category5 = "Shoes"

categories[17]["name"] = clothing_category1
categories[18]["name"] = clothing_category2
categories[19]["name"] = clothing_category3
categories[20]["name"] = clothing_category4
categories[21]["name"] = clothing_category5

lines = []

myfile = open('categories.txt', mode='w') 
myfile.write('\n'.join(str(category) for category in categories))
myfile.close()



