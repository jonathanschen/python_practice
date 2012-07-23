list = [2,3,4,5,6]

def swap_first_last(my_list):
	temp = my_list[1:(len(my_list)-1)]
	temp.append(my_list[0])
	temp.insert(0,my_list[len(my_list)-1])
	print temp
swap_first_last(list)	
	