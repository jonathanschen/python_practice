rolo_data = {'pin': {'address': '8 Thai Rd', 'phone': '+662401924', 'email': 'pnk@gmail.com'},
			'nermis':{'address': 'boogie down', 'phone': '212', 'email': 'nr@gmail.com'}, 
			'kiril':{'address': '12 Sofia', 'phone': '2122401924', 'email': 'kt@gmail.com'}, 
			'cheong': {'address': 'LA bitc', 'phone': '301', 'email': 'ci@gmail.com'}
			}

class Rolodex:
	def displayName(self, name):
		self.name = name
		print name
	def homeAddress(self, name):
		self.name = name
		address1 = rolo_data[self.name]['address']
		print address1
	def phoneNumber(self, name):
		self.name = name 
		phone1 = rolo_data[self.name]['phone']
		print phone1
	def emailAddress(self, name):
		self.name = name	
		email1 = rolo_data[self.name]['email']
		print email1


who = raw_input("Whos contact info are you looking for?(pin, nermis, kiril, or cheong)>>    ")
contact = raw_input("what contact infor do you want for them? (email, address, or phone)>>   ")



if contact == 'name':
	person = Rolodex()
	person.displayName()
elif contact == 'phone':
	person = Rolodex(who)
	person.phoneNumber()
elif contact == 'email':
	person = Rolodex()
	person.emailAddress(who)
elif contact == 'address':
	person = Rolodex()
	person.homeAddress(who)