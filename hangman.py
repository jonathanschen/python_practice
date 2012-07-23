secret_word = 'claptrap'
letters_guessed = []
mistakes_made = 8
max_guesses = 6




def guess_letter():
	guess_letter = raw_input('Go ahead and guess a letter:>>>>> ')
	letters_guessed.append(guess_letter)
	max_guesses = max_guesses - 1
	for i in range(len(secret_word)):
		x = 0
		if secret_word[i] == guess_letter:
			print "it is the %d\'th letter" % (int(i) + 1)
			x += 1
	print "there are % d % s in the word" % (x, guess_letter)
	print "you have % d guesses left" % (max_guesses)
	
	if guess_letter not in secret_word:
		print "Im sorry % s is not in the word :(" % guess
		print "You have % d guesses left" % max_guesses

def guess_word():
	something.readme()

print "Hi there welcome to JC's hangman game!  Are you excited to play?????"

number_of_letters = len(secret_word)

print "The first word has %d letters" % number_of_letters
print "You have 6 chances before your guesses are up and you hang! What would you like to do?"
print "1.Guess letters\n2.Guess word"
decision = int(raw_input(">> "))
if decision == 1:
	guess_letter()
elif decision == 2:
	guess_word()