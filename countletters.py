a_counter = raw_input("Type a sentence and i'll count the a\'s!    ")

def countLetter(a_counter):
	number_of_a = 0
	for a in a_counter:
		if a == 'a':
			number_of_a +=1
	print number_of_a

countLetter(a_counter)