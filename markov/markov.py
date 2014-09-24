import re
import random

words = ''

with open('seed.txt', 'r') as seed:
	for line in seed:
		words += line

wordlist = re.findall(r"[\w']+", words)

worddict = dict()

prev = ''
for word in wordlist:
	if prev is '':
		prev = word
		continue

	if prev in worddict:
		worddict[prev].append(word)
	else:
		worddict[prev] = [word]

	prev = word

word = random.choice(list(worddict.keys()))

sentence = word
while True:
	if word not in list(worddict.keys()): break
	word = random.choice(worddict[word])
	sentence += ' ' + word

print(sentence)