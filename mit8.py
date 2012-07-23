A = "gtggcaacgtgc" 
B = "gtagcagcgcgc" 
C = "gcggcacagggt" 
D = "gtgacaacgtgc"

def compare(set_1, set_2):
	count = 0
	for i in range(len(A)):
		if set_1[i] != set_2[i]:
			count = count + 1
			
	print "the final count is", count
		
	
print_this = compare(A, B)
print print_this