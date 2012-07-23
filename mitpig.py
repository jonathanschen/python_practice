vowels = ['a', 'e', 'i', 'o', 'u']

sentence = raw_input("What is the sentence you want me to convert(please use only words and spaces)?    ")

def starts_with_vowel(word):
	while word[0] in vowels:
		return True
	else:
		return False

def sentence_splitter(sentence):
	split_sentence = sentence.split(' ')
	return split_sentence

def sentence_converter(starts_with_vowel, sentence_splitter):
	convert_this = sentence_splitter(sentence)
	for _word in convert_this:
		if starts_with_vowel(_word) == True:  
			translated_word = _word + 'hay' 
			print translated_word
		else:
			translated_word = _word[1:] + 'hay'
			print translated_word
						
sentence_converter(starts_with_vowel, sentence_splitter)