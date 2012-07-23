import math

test_cases = [1, 9, -3]
test_case_answers = [1, 3, 0]

def custom_sqrt(num):
	if num >= 0:
		return math.sqrt(num)
	else:
		return 0
for i in range(len(test_cases)):
	if custom_sqrt(test_cases[i]) != test_case_answers[i]:
		print "Test Case #", i, "failed!"


custom_sqrt(test_cases)