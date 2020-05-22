vowels='aeiou'
counter=0

def word_enter():
	return input('Please write a word: ')

def special(letter):
	return letter in vowels

def count(counter, word):
	for letter in word:
		if special(letter):
			counter += 1
		return counter

def write_screen(word):
	message = "In the word \"{}\" there are {} vowels."
	print(message.format(word, count(counter, word)))

def run():
	word = word_enter()
	write_screen(word)
