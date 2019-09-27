import itertools
import urllib.request, json

# 10k most common words
def initialize_database_one():
	# initialize a set for fast lookups
	english_vocab = set()

	# get the text file that contains english words
	data = urllib.request.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')
	
	# traverse through the data and add to the set
	for line in data:
		english_vocab.add(line[:-1].decode('UTF-8'))
	
	return english_vocab


# 400k+ word dictionary
def initialize_database_two():
	url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"

	# get the json file that contains english words
	response = urllib.request.urlopen(url)
	english_vocab = dict(json.loads(response.read()))

	# return a set of words, for fast lookups
	return set(english_vocab.keys())

def process(letters, min_length, english_vocab):
	words_tuples = []
	words = []
	to_return = set()

	# create all combinations of the letters and append it to a list
	for i in range(len(letters)):
		words_tuples.append(list(itertools.permutations(letters, i+1)))

	# check if the combination of letters is in the dictionary
	for ls in words_tuples:
		for tup in ls:
			word = ''
			for letter in tup:
				word += letter
			words.append(word)

	# makes sure the list of valid words satisfies the length requirement
	for word in words:
		if word in english_vocab and len(word) >= min_length:
			to_return.add(word)

	return to_return


if __name__ == '__main__':
	# inputs
	letters = ['p', 'm', 'o', 'a', 's', 't']
	min_length = 3

	# databases 1
	english_vocab = initialize_database_one()
	solution1 = process(letters, min_length, english_vocab)
	print('Database One:\n', solution1)

	print('\n')

	# database 2
	english_vocab = initialize_database_two()
	solution = process(letters, min_length, english_vocab)
	solution2 = set()

	# return words that in database 2 that are not already in database 1
	for word in solution:
		if word not in solution1:
			solution2.add(word)

	print('Addition Words From Database Two:\n', solution2)
