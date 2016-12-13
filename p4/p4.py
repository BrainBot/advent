import re
import string
from collections import defaultdict

def rot_n(word, n):
	lc = string.ascii_lowercase
	n = n % 26
	trans = string.maketrans("-" + lc, " " + lc[n:] + lc[:n] )
	return string.translate(word, trans)

# Read input and prep it
input = open('p4.input.txt')

lines = input.read().split()

regex_str = r"([a-z\-]*)-([\d]*)\[([a-z]*)\]"

regex = re.compile(regex_str)

sector_sum = 0

possible_lines = open('p4.output', 'w')

for line in lines:
	valid = True
	name, sector, check = regex.findall(line)[0]
	letter_freq = {}

	for l in name:
		if l == '-':
			continue
		cur_l = letter_freq.get(l, 0)
		letter_freq[l] = cur_l + 1
	
	sorted_l_freq = sorted(letter_freq, key=letter_freq.__getitem__, reverse=True)

	# invert the letter_freq
	inv_l_freq = defaultdict(list)
	for k, v in letter_freq.iteritems():
		inv_l_freq[v].append(k)
	
	# look at the checksum
	for c in check:
		head_l = sorted_l_freq[0]
		
		# if max is at head, then next
		if head_l == c:
			sorted_l_freq.pop(0)
			continue
		# if letter val is same as head
		elif c in inv_l_freq[letter_freq[head_l]]:
			sorted_l_freq.pop(sorted_l_freq.index(c))
			continue 
		# letter val not next most common
		else:
			valid = False
	
	if valid:
		sector_sum += int(sector)
		possible_lines.write("%s %s\n" % (rot_n(name, int(sector)), sector))

	#print sector_sum
	
