from random import choice
plays = ['rock', 'paper', 'scissor']



player_plays = raw_input("what would you like to play (rock, paper or scissor)?>>     ")


	
def rock():
	computer_plays = choice(plays)
	if computer_plays == 'scissor':
		print "you win computer played scissor"
	elif computer_plays == 'paper':
		print "you lost computer played paper"
	elif computer_plays == 'rock':
		while computer_plays == player_plays:
			print "You picked the same thing.  Play again"
			player_plays = raw_input("what would you like to play (rock, paper or scissor)?>>     ")
			computer_plays = choice(plays)
		if player_plays == 'rock':
			rock()
		elif player_plays == 'scissor':
			scissor()
		elif player_plays == 'paper':
			paper()			
				
def scissor():
		computer_plays = choice(plays)
		if computer_plays == 'rock':
			print "you lost computer played rock"
		elif computer_plays == 'paper':
			print "you won computer played paper"
		else:
			while player_plays == computer_plays:
				print "You picked the same thing.  Play again"
				computer_plays = choice(plays)
				player_plays = raw_input("what would you like to play (rock, paper or scissor)>>     ")
				player_plays()
				
def paper():
		computer_plays = choice(plays)
		if computer_plays == 'scissor':
			print "you lost computer played scissor"
		elif computer_plays == 'rock':
			print "you won computer played rock"
		else:
			while player_plays == computer_plays:
				print "You picked the same thing.  Play again"
				computer_plays = choice(plays)
				player_plays = raw_input("what would you like to play (rock, paper or scissor)>>     ")
				player_plays()
				

if player_plays == 'paper':
	paper()
elif player_plays == 'scissor':
	scissor()
elif player_plays == 'rock':
	rock()