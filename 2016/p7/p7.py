import re

f = open("p7.input")

support = 0

lines = [l.strip() for l in f.readlines()]

def supports_abba(s):
	start = 0
	while start + 4 <= len(s):
		if s[start] != s[start+1] and \
		s[start] == s[start+3] and \
		s[start+1] == s[start+2]:
			return True
		start += 1 
	return False

def split_ipv7(s):
	cur = 0
	word_start = 0
	# list of form [<normal>][<inside brackets>]
	results = [list(),list()]

	while cur < len(s):
		if s[cur] == '[':
			results[0].append(s[word_start:cur])
			word_start = cur + 1
		elif s[cur] == ']':
			results[1].append(s[word_start:cur])
			word_start = cur + 1
		cur += 1

	# handle end of string
	results[0].append(s[word_start:cur])
	return results



for l in lines:
	split_line = split_ipv7(l)
	#print split_line
	if any([supports_abba(seg) for seg in split_line[0]]) and not any([supports_abba(seg) for seg in split_line[1]]):
		support += 1

print support
