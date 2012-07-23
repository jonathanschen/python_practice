list = [1, 10, 12, 50, 6, 1, 9]

def find_max_element(my_list):
	my_list.sort()
	print my_list[len(my_list)-1]
	
find_max_element(list)