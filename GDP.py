import csv
import math

unemp_dict = {}
average_list = []
file_name_unemp = open('unemp.csv', 'rU')
first_file = list(file_name_unemp)


def ann_unemp(year):
	string = first_file[year-1947]
	string = string[1:-1].split(',')
	string = string[1:-1]
	new_string = []
	for i in string:
		new_string.append(float(i))
	total = sum(new_string)
	average = total/12
	return average

y = ann_unemp(1950)
print y



