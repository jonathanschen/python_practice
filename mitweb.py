NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19] 
people = {}
ages_people = []

for i in range(len(NAMES)):
	people[i] = {NAMES[i]:AGES[i]}
		
def in_age_return_person(age):
	x = 0
	for i in AGES:
		if i == age:
			person = NAMES[x]
			ages_people.append(person)
		x += 1			


		


 
	