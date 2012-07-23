import pickle
from operator import itemgetter

open_stop = open('stopwords.txt', 'rU')
open_txt = open('debate.txt', 'rU')
stop_list = list(open_stop)
stop_list = [words.rstrip() for words in stop_list] 
stop_list.append('biden:')
stop_list.append('palin:')


palin = []
biden = []

palin_counter = {}
biden_counter = {}

lines = open_txt.readlines()
for line in lines:
	if 'PALIN:' in line:
		palin.append(line)
	elif 'BIDEN:' in line:
		biden.append(line)

def manipulate_list(person):
	person = [person[i].split() for i in range(len(person))]
	person = [inner for outer in person for inner in outer]
	return person

def delete_stop_words(stop_list, person):
	new_list = [words for words in person if words.lower() not in stop_list]
	return new_list

palin = manipulate_list(palin)
palin = delete_stop_words(stop_list, palin)
biden = manipulate_list(biden)
biden = delete_stop_words(stop_list, biden)

for word in palin:
	if word not in palin_counter:
		palin_counter[word] = 1
	elif word in palin_counter:
		palin_counter[word] = palin_counter[word] + 1

for word in biden:
	if word not in biden_counter:
		biden_counter[word] = 1
	elif word in biden_counter:
		biden_counter[word] = biden_counter[word] + 1

biden_sorted = sorted(biden_counter.items(), key=lambda x: x[1])
palin_sorted = sorted(palin_counter.items(), key=lambda x: x[1])

top_40_palin = palin_sorted[(len(palin_sorted)-40):len(palin_sorted)]
top_40_biden = biden_sorted[(len(biden_sorted)-40):len(biden_sorted)]

print top_40_palin

open_stop.close()
open_txt.close()

#filename = open("palin.html", 'w')
#filename.writelines(top_40_palin)
#filename.close()
#filename1 = open("biden.html", 'w')
#filename1.writelines(top_40_biden)
#filename1.close()






#print palin_string