hour_1 = int(raw_input("what is the hour(1)?   "))
minute_1 = int(raw_input("what is the minute(1)?   "))
seconds_1 = int(raw_input("what is the seconds(1)?   "))

hour_2 = int(raw_input("what is the hour(2)?   "))
minute_2 = int(raw_input("what is the minute(2)?   "))
seconds_2 = int(raw_input("what is the seconds(2)?   "))

t1 = {'hour': hour_1, 'minute': minute_1, 'seconds': seconds_1}
t2 = {'hour': hour_2, 'minute': minute_2, 'seconds': seconds_2}

def hour_comp(t1, t2):
	if t1['hour'] > t2['hour']:
		print "True"
	elif t1['hour'] < t2['hour']:
		print "False"
	else:
		minutes_comp(t1,t2)
		
def minutes_comp(t1, t2):
	if t1['minute'] > t2['minute']:
		print "True"
	elif t1['minute'] < t2['minute']:
		print "False"
	else:
		seconds_comp(t1,t2)

def seconds_comp(t1, t2):
	if t1['seconds'] > t2['seconds']:
		print "True"
	elif t1['seconds'] < t2['seconds']:
		print "False"
	else:
		print "They are equal"

hour_comp(t1, t2)