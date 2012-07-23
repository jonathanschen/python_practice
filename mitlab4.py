_large_prime = 137
_KEY = 99
guesses = 0



while guesses < 3:
	pw = raw_input("Please enter your password...")
	attempt = hash(pw)
	converted1 = attempt%_large_prime

	if converted1 == _KEY:
		print "you got it"
		exit(0)
	elif converted1 != _KEY:
		print "Try again"
		guesses += 1
print "You dont know the password"

	


