list = []

#def is_valid(num):
# return(num >= 0)

#while not is_valid:
#	num = int(raw_input('Please input a positive integer...'))
#	if not is_valid(num):
#		print "Please enter a valid number"
#i = 0
#while i < 10:
	
#	num = int(raw_input('>>> '))
#	list.append(num)
#	i = i + 1

#sort_list(biggest)

list = [1, 5, 12, 3]

def sort_list(x, position):
	for i in x:
		biggest = max(x)
		print "The biggest number is", biggest
		x[position] = biggest 
		print x
		print position

sort_list(list, first)
