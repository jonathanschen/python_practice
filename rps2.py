from random import choice
plays = ['rock', 'paper', 'scissor']
cp = choice(plays)

pp_score = 0
cp_score = 0
pp_rock = 0
pp_scissor = 0
pp_paper = 0
pp = raw_input('>Make a move player...  ')
if pp == 'rock':
	pp_rock += 1
elif pp == 'scissor':
	pp_scissor += 1
elif pp == 'paper':
	pp_paper += 1
	

def favors():
	if pp_scissor > pp_paper and pp_paper >= pp_rock:
		return 'slover'
	if pp_scissor > pp_rock and pp_rock >= pp_paper:
		return 'slover'
	elif pp_paper > pp_rock and pp_rock >= pp_scissor:
		return 'plover'
	elif pp_paper > pp_rock and pp_rock >= pp_scissor:
		return 'plover'
	elif pp_rock > pp_scissor and pp_scissor >= pp_paper:
		return 'rlover'
	elif pp_rock > pp_paper and pp_paper >= pp_scissor:
		return 'rlover'
	elif pp_rock == pp_scissor == pp_paper:
		return 'neutral'
	elif (pp_rock == pp_paper) and pp_rock > pp_scissor:
		return 'neutral'
	elif (pp_paper == pp_scissor) and pp_paper > pp_rock:
		return 'neutral'
	

while ('q' or 'quit') != pp:
	while cp == pp:
		print "tie"
		pp = raw_input('>Make a move player...     ')
		if pp == 'rock':
			pp_rock += 1
		elif pp == 'scissor':
			pp_scissor += 1
		elif pp == 'paper':
			pp_paper += 1
		favor = favors()
		if favor == 'neutral':
			cp = choice(plays) 
		elif favor == 'slover':
			cp = 'rock'
		elif favor == 'rlover':
			cp = 'paper'
		elif favor == 'plover':
			cp = 'scissor'	
	if pp == 'rock':
		if cp == 'scissor':
			print "you win he picked scissor"
			pp_score +=1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'	
		elif cp == 'paper': 
			print "lost he picked paper"
			cp_score += 1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'		
	elif pp == 'scissor':
		if cp == 'paper':
			print "you win he picked paper"
			pp_score += 1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'	
		elif cp == 'rock': 
			print "lost he picked rock"
			cp_score +=1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'	
	elif pp == 'paper':
		if cp == 'rock':
			print "you win he picked rock"
			pp_score += 1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'	
		elif cp == 'scissor': 
			print "lost he picked scissor"
			cp_score += 1
			pp = raw_input('>Make a move player...  ')
			if pp == 'rock':
				pp_rock += 1
			elif pp == 'scissor':
				pp_scissor += 1
			elif pp == 'paper':
				pp_paper += 1
			favor = favors()
			if favor == 'neutral':
				cp = choice(plays) 
			elif favor == 'slover':
				cp = 'rock'
			elif favor == 'rlover':
				cp = 'paper'
			elif favor == 'plover':
				cp = 'scissor'	
print "Game OVER!!!"
print "player 1 score:", pp_score, "computer score:", cp_score
print "player i paper plays:",pp_paper, "rock plays:",pp_rock, "scissorplays:",pp_scissor