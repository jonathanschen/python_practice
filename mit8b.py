import math

A = "gtggcaacgtgc" 
B = "gtagcagcgcgc" 
C = "gcggcacagggt" 
D = "gtgacaacgtgc"

def compare(set_1, set_2):
	count_a1 = set_1.count('a')
	count_a2 = set_2.count('a')
	count_t1 = set_1.count('t')
	count_t2 = set_2.count('t')
	count_g1 = set_1.count('g')
	count_g2 = set_2.count('g')
	count_c1 = set_1.count('c')
	count_c2 = set_2.count('c')

	diff_A = math.fabs(count_a1 - count_a2)
	diff_T = math.fabs(count_t1 - count_t2)
	diff_G = math.fabs(count_g1 - count_g2)
	diff_C = math.fabs(count_c1 - count_c2)
	
	print "diff A:", diff_A
	print "diff T:", diff_T
	print "diff G:", diff_G
	print "diff C:", diff_C
	
compare(A, B)