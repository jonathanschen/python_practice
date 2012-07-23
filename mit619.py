list = [1, 4, 8, 9]

def all_under_6(my_list):
	under_6 = True
	for i in my_list:
		if i >=6:
			print "False"
			
	return under_6
print under_6
print(my_list)

all_under_6(list)