users = []

#create input for all items
for x in range(0, 15):
	user = {'username': ("user"+str(x)), 'password': "12345", 'phone_number': "8147777777", 'email': "user" + str(x) + "@gmail.com", 'review': ""} 
	users.append(user)

myfile = open('users.txt', mode='w') 
myfile.write('\n'.join(str(user) for user in users))
myfile.close()