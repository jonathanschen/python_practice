def favors():
	if pp_scissor > pp_paper and pp_paper >= pp_rock:
		return 'slover'
	elif pp_paper > pp_rock and pp_rock >= pp_scissor:
		return 'plover'
	elif pp_rock > pp_scissor and pp_scissor >= pp_paper:
		return 'rlover'
	elif pp_rock == pp_scissor == pp_paper:
		return 'neutral'
	elif (pp_rock == pp_paper) and pp_rock > pp_scissor:
		return 'neutral'
	elif (pp_paper == pp_scissor) and pp_paper > pp_rock:
		return 'neutral'

pp_rock = 2
pp_paper = 6
pp_scissor = 2 

favor = favors()
print favor
