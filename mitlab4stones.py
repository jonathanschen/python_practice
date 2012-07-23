start_pile = 100
max = 5
total_pile = start_pile
p1 = []
p2 = []

while total_pile <= 100:
	p1_turn = int(raw_input("P1 pick a number between 1 and 5:  "))
	while p1_turn > max:
		print "Your response needs to between 1 and 5"
		p1_turn = int(raw_input("P1 pick a number between 1 and 5:  "))
	while p1_turn <= 0:		
			print "Your response needs to between 1 and 5"
			p1_turn = int(raw_input("P1 pick a number between 1 and 5:  "))
	while p1_turn > total_pile:
		print "there aren't that many stones left"
		p1_turn = int(raw_input("P1 pick a number between 1 and 5:  "))
	p1.append(p1_turn)
	total_p1 = sum(p1)
	total_p2 = sum(p2)
	total_pile = total_pile - (p1_turn)
	print "There are %d total stones remaining" % total_pile 
	if total_pile == 0:
		print "You picked the last stone, you win!!!"
		break
	p2_turn = int(raw_input("P2 pick a number between 1 and 5:  "))
	while p2_turn > max:
		print "Your response needs to between 1 and 5"
		p2_turn = int(raw_input("P2 pick a number between 1 and 5:  "))
	while p2_turn <= 0:		
			print "Your response needs to between 1 and 5"
			p2_turn = int(raw_input("P2 pick a number between 1 and 5:  "))
	while p2_turn > total_pile:
		print "there aren't that many stones left"
		p2_turn = int(raw_input("P2 pick a number between 1 and 5:  "))
	p2.append(p2_turn)
	total_p1 = sum(p1)
	total_p2 = sum(p2)
	total_pile = total_pile - (p2_turn)
	print "There are %d total stones remaining" % total_pile 
	if total_pile == 0:
		print "You picked the last stone.  You win!!"
		break
print "Game Over"
