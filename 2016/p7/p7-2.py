import re

f = open("p7.input")

support = 0

lines = [l.strip() for l in f.readlines()]

def find_aba(s):
	start = 0
	results = []
	while start + 3 <= len(s):
		if s[start] != s[start+1] and \
		s[start] == s[start+2]:
			results.append(s[start:start+3])
		start += 1 
	return results


def has_bab(aba, s):
	print aba, s
	result = False
	for a in aba:
		cand = a[1] + a[0] + a[1]
		result |= True if s.find(cand) > -1 else False
	return result



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
	aba_cand = []

	for seg in split_line[0]:
		aba_cand.extend(find_aba(seg))

	if any(has_bab(aba_cand, s) for s in split_line[1]):
		support += 1


print support
