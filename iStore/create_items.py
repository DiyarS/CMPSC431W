lines = []

#create input for all items
for x in range(0, 100):
	line = {'item_id': x, 'description': "Description will go here", 'location': "Earth, Milky Way", 'rating': 1.0} 
	lines.append(line)

myfile = open('input_items.txt', mode='w') 
myfile.write('\n'.join(str(line) for line in lines))
myfile.close()

