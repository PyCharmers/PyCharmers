import re
import random

words = ''

with open('seed.txt', 'r') as seed:
	for line in seed:
		words += line

wordlist = re.findall(r"[\w']+[\".,;:]?", words)

worddict = dict()

prev = (wordlist[0], wordlist[1])
for i in range(2, len(wordlist)):
	word = wordlist[i]
	if prev in worddict:
		worddict[prev].append(word)
	else:
		worddict[prev] = [word]

	prev = (prev[1], word)

prefix = 'a'
while not prefix[0].isupper():
	prefix = random.choice(list(worddict.keys()))

i = 0
sentence = prefix[0] + ' ' + prefix[1]
while True:
	if prefix not in list(worddict.keys()):
		sentence += '.'
		break
	if '.' in prefix[1]: break
	prefix = (prefix[1], random.choice(worddict[prefix]))
	sentence += ' ' + prefix[1]
	i += 1

print(sentence)