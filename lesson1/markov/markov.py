# Import the Regular Expressions (Regex) module 
import re
# Import the Random Module
import random

# Initialize an empty string to which we will add words
words = ''

# Open the file 'seed.txt' in the current folder and refer to is as 'seed'
with open('seed.txt', 'r') as seed:
	# loop through each line of text in the file
	for line in seed:
		# and concatenate the line to the 'words' string
		words += line

# This is a regex method which will search through the 'words' string
# and return a list of all the substrings that match a certain pattern.
# The pattern will match all instances of whitespace-separated words that
# may end with a quote, period, comma, semi-colon, or colon.
wordlist = re.findall(r"[\w']+[\".,;:]?", words)

# Create a new dictionary (a set of key->value pairs)
worddict = dict()

# Store the first two words in the text as a tuple
prev = (wordlist[0], wordlist[1])

# Iterate the i variable from 2 through the number of words in 'wordlist' 
for i in range(2, len(wordlist)):
	# Get the ith word in the wordlist
	word = wordlist[i]
	# If the last two words are already a key in the dictionary
	if prev in worddict:
		# Add the ith word in the wordlist to a list of words that follow the last two words
		worddict[prev].append(word)
	# If the last two words are not a key in the dictionary
	else:
		# Set the last two words as a key in the dictionary that points
		# to a value of a list of one word, the current word 
		worddict[prev] = [word]
	# Set the 'prev' variable to be the last previous word, and the current word
	# before the next iteration begins
	prev = (prev[1], word)

# Initialize 'prefix' as a lowercase string
prefix = 'a'
# While the first letter of 'prefix' is not capitalized
while not prefix[0].isupper():
	# Pick a random word pair from list of all the words that are keys of the dictionary
	prefix = random.choice(list(worddict.keys()))

i = 0
# Start the sentence wth the random word pair selected above
sentence = prefix[0] + ' ' + prefix[1]
# Loop forever (until a break command)
while True:
	# If the second word in the pair contains a period, end the loop
	if '.' in prefix[1]: break
	# Set a new prefix that contains the 2nd word from the current prefix, and a
	# new word that is randomly chosen from the words that follow the current pair.
	prefix = (prefix[1], random.choice(worddict[prefix]))
	# Add a space and the 2nd word from the prefix pair to the sentence string.
	sentence += ' ' + prefix[1]
	# Increment the counter to index further
	i += 1

# Print the sentence to the terminal
print(sentence)

# Example output (seed.txt = Hamlet):
"""
 I do not fear our person: There's such divinity doth hedge a king, That treason can
 but peep to what it would, Acts little of his soul, When he is the very substance of
 the thing, each word made true and good, The apparition comes: I knew him, Horatio; a
 fellow whipped for o'erdoing Termagant; it out herods Herod: pray you go to seek him out; 
 speak fair, and bring them in.

 He is a murderer and a gentleman.

 I heard, and do in part believe it.
"""
