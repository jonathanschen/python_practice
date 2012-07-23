a = [1, 2, 3]
b = []
def cumulative_sum(n):
	x = 0
	for i in n:
		x += i
		b.append(x)		
	print b
	
	
	
	
cumulative_sum(a)